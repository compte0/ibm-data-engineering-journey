import asyncio
import json
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
from datetime import datetime # Importation nécessaire pour datetime

# --- Configuration du proxy Bright Data ---
AUTH = 'brd-customer-hl_9edf8c10-zone-scraping_browser1:2usy01m79r4m' # Garde tes propres identifiants ici
SBR_WS_CDP = f'wss://{AUTH}@brd.superproxy.io:9222'

# --- Liste des URLs à scraper ---
# Ces URLs pointent vers des pages de produits spécifiques sur le site codeavecjonathan.com
URLS = [
    'https://codeavecjonathan.com/scraping/techsport/', # Page d'accueil ou produit par défaut
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=fitness-pro',
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=solar-sync',
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=tech-wizard'
]

# --- Paramètres de sortie JSON ---
JSON_DATA_FILE = 'techsport_products.json' # Nom du fichier JSON de sortie
DATE_TODAY = datetime.today()
DATE_TODAY_STR = DATE_TODAY.strftime('%Y-%m-%d') # Format YYYY-MM-DD pour une meilleure organisation

# --- Mode BYPASS pour le développement/test ---
# Si True, le script ne se connecte pas au proxy/navigateur.
# Il essaie de lire le HTML depuis 'scraping-browser.html' (pour un test rapide).
# Si False, il effectue le scraping réel via Playwright et Bright Data.
BYPASS = True

# --- Fonctions d'extraction ---

def affiche_texte_si_non_vide(element_bs):
    """
    Extrait le texte d'un élément BeautifulSoup s'il existe, le nettoie (strip),
    et retourne None si l'élément est vide ou non trouvé.
    """
    if element_bs:
        return element_bs.text.strip()
    return None

def extraction_product_page_infos(html_content, url_scraped):
    """
    Extrait les informations spécifiques d'une page de produit TechSport.
    Prend le contenu HTML et l'URL de la page en entrée.
    Retourne un dictionnaire avec les informations extraites.
    """
    infos = {"url": url_scraped} # Inclut l'URL dans les données extraites
    bs = BeautifulSoup(html_content, 'html5lib') # Utilise html5lib pour un parseur robuste

    # Extraction du titre du produit
    infos['title'] = affiche_texte_si_non_vide(bs.find('span', id='productTitle'))

    # Extraction du nombre d'avis (ratings)
    ratings_text = affiche_texte_si_non_vide(bs.find('span', id='customer-review-text'))
    if ratings_text:
        # Tente d'extraire le premier nombre de la chaîne (ex: "125 avis client")
        rnb_ratings_str = ratings_text.split()[0]
        if rnb_ratings_str.isdigit(): # Vérifie si c'est bien un nombre
            infos['nb_ratings'] = int(rnb_ratings_str)
        else:
            infos['nb_ratings'] = None # Si ce n'est pas un nombre, met à None
    else:
        infos['nb_ratings'] = None # Si le texte des avis n'est pas trouvé

    # Extraction du prix
    price_whole_str = affiche_texte_si_non_vide(bs.find('span', class_='price-whole'))
    price_fraction_str = affiche_texte_si_non_vide(bs.find('span', class_='price-fraction'))
    price = None
    if price_whole_str and price_whole_str.isdigit():
        try:
            price = float(price_whole_str)
            if price_fraction_str and price_fraction_str.isdigit():
                price += (float(price_fraction_str) / 100)
            infos['price'] = price
        except ValueError:
            infos['price'] = None # En cas d'erreur de conversion
    else:
        infos['price'] = None # Si la partie entière du prix n'est pas trouvée ou n'est pas un nombre

    # Extraction de la description
    infos['description'] = affiche_texte_si_non_vide(bs.find('div', id="product-description"))

    return infos

# --- Fonction principale de scraping asynchrone ---

async def run(pw):
    all_scraped_data = [] # Liste pour stocker les données de toutes les pages

    browser = None # Initialise le navigateur à None
    if not BYPASS:
        print('Connecting to Bright Data Browser API...')
        browser = await pw.chromium.connect_over_cdp(SBR_WS_CDP)
    else:
        print("Mode BYPASS activé : Le scraping réel via le navigateur est désactivé.")
        print("Pour les tests, assurez-vous que 'scraping-browser.html' contient le HTML d'une page à analyser.")

    try:
        # Boucle sur chaque URL à scraper
        for i, url in enumerate(URLS):
            print(f"\n--- Traitement de la page {i+1}/{len(URLS)} : {url} ---")
            html_content = None # Initialise le contenu HTML pour chaque itération

            if not BYPASS:
                # Si le mode BYPASS est désactivé, on se connecte au navigateur
                if browser is None:
                    # Ceci ne devrait pas arriver si la connexion initiale a réussi
                    raise Exception("Le navigateur n'est pas connecté alors que BYPASS est False.")
                
                page = await browser.new_page() # Ouvre un nouvel onglet pour chaque URL
                try:
                    print(f'Navigation vers : {url}')
                    # Attend que le DOM soit chargé pour s'assurer que le contenu est là
                    await page.goto(url, wait_until='domcontentloaded')
                    
                    # Optionnel : prendre une capture d'écran pour le debug
                    # Nomme la capture d'écran de manière unique pour chaque page
                    # try:
                    #     screenshot_name = url.replace('https://', '').replace('/', '_').replace('?', '_').replace('=', '_')
                    #     await page.screenshot(path=f"screenshots/{screenshot_name}.png", full_page=True)
                    #     print(f"Capture d'écran sauvegardée pour {url}")
                    # except Exception as e_ss:
                    #     print(f"Impossible de prendre la capture d'écran pour {url}: {e_ss}")

                    html_content = await page.content() # Récupère le HTML complet de la page
                    # print(html_content[:500]) # Affiche les 500 premiers caractères du HTML pour debug
                except Exception as e_page:
                    print(f"Erreur lors de la navigation ou de la récupération HTML pour {url}: {e_page}")
                    html_content = None # Assure que html_content est None en cas d'erreur
                finally:
                    if page: # S'assure que la page a été créée avant de tenter de la fermer
                        await page.close() # Ferme l'onglet après traitement
            else:
                # En mode BYPASS, tente de lire le HTML depuis un fichier local
                # Note : Pour que BYPASS fonctionne bien avec plusieurs URLs,
                # il faudrait que tu aies des fichiers HTML locaux pré-enregistrés
                # nommés de manière cohérente avec chaque URL.
                # Ici, pour la simplicité, on suppose un fichier générique de test.
                try:
                    with open('scraping-browser.html', 'r', encoding='utf-8') as f:
                        html_content = f.read()
                    print("Utilisation du contenu HTML depuis 'scraping-browser.html' (mode BYPASS).")
                except FileNotFoundError:
                    print(f"Attention : 'scraping-browser.html' non trouvé pour le mode BYPASS. Passage à l'URL suivante.")
                    continue # Passe à l'URL suivante si le fichier n'existe pas

            if html_content: # Procède à l'extraction si le HTML a été obtenu
                print('Extraction des informations...')
                # Appelle ta fonction d'extraction avec le HTML et l'URL courante
                infos = extraction_product_page_infos(html_content, url)
                infos["date_extraction"] = DATE_TODAY_STR # Ajoute la date d'extraction
                all_scraped_data.append(infos) # Ajoute les données extraites à la liste globale
                print(f"Données extraites pour {url}: {infos}")
            else:
                print(f"Aucun contenu HTML à extraire pour {url}. Données non ajoutées.")

    except Exception as e_run:
        print(f"Une erreur inattendue est survenue pendant l'exécution du scraping : {e_run}")

    finally:
        if browser: # S'assure que le navigateur a été ouvert avant de tenter de le fermer
            await browser.close()
            print('Navigateur fermé.')

    # --- Sauvegarder toutes les données collectées dans un seul fichier JSON ---
    try:
        if all_scraped_data: # Sauvegarde seulement s'il y a des données
            with open(JSON_DATA_FILE, 'w', encoding='utf-8') as f:
                # json.dump convertit la liste de dictionnaires Python en JSON
                # ensure_ascii=False permet de conserver les caractères spéciaux (accents)
                # indent=4 rend le fichier JSON lisible avec des indentations
                json.dump(all_scraped_data, f, ensure_ascii=False, indent=4)
            
            print(f"\n--- Scraping terminé ---")
            print(f"Toutes les données collectées ({len(all_scraped_data)} éléments) ont été sauvegardées dans '{JSON_DATA_FILE}'")
        else:
            print("\n--- Scraping terminé ---")
            print("Aucune donnée n'a été collectée pour être sauvegardée.")

    except Exception as e_json:
        print(f"Une erreur est survenue lors de la sauvegarde des données JSON : {e_json}")

# --- Point d'entrée du programme asynchrone ---
async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())
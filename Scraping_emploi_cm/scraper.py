import requests
import os
from datetime import datetime
import re
import brotli

def scrape_emploi_cm():
    """
    Script de scraping pour le site emploi.cm
    Récupère le HTML de la page de recherche d'emplois et le sauvegarde
    """
    
    # URL cible - page de recherche d'emplois
    url = "https://www.emploi.cm/recherche-jobs-cameroun"
    
    # Headers personnalisés avec User-Agent pour le scraping
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 - Web Scraper Bot - Contact: chrisdavebenge@gmail.com - Purpose: Data Collection for Research',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate',  # Retirons 'br' pour éviter la compression Brotli
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Cache-Control': 'max-age=0',
    }
    
    try:
        print(f"Tentative de connexion à {url}...")
        print(f"User-Agent: {headers['User-Agent']}")
        
        # Faire la requête HTTP
        response = requests.get(url, headers=headers, timeout=30)
        
        # Vérifier le statut de la réponse
        response.raise_for_status()
        
        print(f"Connexion réussie! Statut: {response.status_code}")
        print(f"Taille du contenu brut: {len(response.content)} bytes")
        print(f"Encodage: {response.encoding}")
        print(f"Content-Encoding: {response.headers.get('Content-Encoding', 'Aucun')}")
        
        # Gérer la décompression si nécessaire
        if response.headers.get('Content-Encoding') == 'br':
            print("Décompression Brotli en cours...")
            try:
                html_content = brotli.decompress(response.content).decode('utf-8')
            except Exception as e:
                print(f"Erreur lors de la décompression Brotli: {e}")
                html_content = response.text
        else:
            html_content = response.text
        
        # Créer un nom de fichier avec timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"emploi_cm_recherche_{timestamp}.html"
        
        # Sauvegarder le HTML dans un fichier
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"HTML sauvegardé dans le fichier: {filename}")
        print(f"Taille du fichier sauvegardé: {len(html_content)} caractères")
        
        # Afficher quelques informations sur le contenu
        print(f"\nInformations sur la page:")
        print(f"- Titre de la page: {extract_title(html_content)}")
        print(f"- Nombre de caractères: {len(html_content)}")
        print(f"- Encodage détecté: {response.encoding}")
        
        # Afficher les premières lignes du contenu
        print(f"\nPremières lignes du contenu:")
        lines = html_content.split('\n')[:5]
        for i, line in enumerate(lines, 1):
            print(f"{i}: {line[:100]}...")
        
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la requête: {e}")
        return False
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return False

def extract_title(html_content):
    """
    Extrait le titre de la page HTML avec une méthode plus robuste
    """
    try:
        # Méthode 1: Recherche du tag title
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html_content, re.IGNORECASE | re.DOTALL)
        if title_match:
            return title_match.group(1).strip()
        
        # Méthode 2: Recherche de h1
        h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE | re.DOTALL)
        if h1_match:
            return h1_match.group(1).strip()
        
        # Méthode 3: Recherche de meta title
        meta_title_match = re.search(r'<meta[^>]*name=["\']title["\'][^>]*content=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
        if meta_title_match:
            return meta_title_match.group(1).strip()
        
        return "Titre non trouvé"
    except Exception as e:
        return f"Erreur lors de l'extraction du titre: {e}"

if __name__ == "__main__":
    print("=== Script de Scraping emploi.cm ===")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 40)
    
    success = scrape_emploi_cm()
    
    if success:
        print("\n✅ Scraping terminé avec succès!")
    else:
        print("\n❌ Échec du scraping")


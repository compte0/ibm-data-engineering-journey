import asyncio
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import json

AUTH = 'brd-customer-hl_9edf8c10-zone-scraping_browser1:2usy01m79r4m'
SBR_WS_CDP = f'wss://{AUTH}@brd.superproxy.io:9222'
#url = 'https://codeavecjonathan.com/scraping/techsport/'

URLS = [
    'https://codeavecjonathan.com/scraping/techsport/',
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=fitness-pro',
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=solar-sync',
    'https://codeavecjonathan.com/scraping/techsport/index.html?id=tech-wizard'
]



def affiche_texte_si_non_vide(texte):
    if texte:
        return texte.text.strip()
    return None

def extraction_product_page_infos(html):
    infos = {}
# bibliothèque
    bs =  BeautifulSoup(html, 'html5lib')

#extraction du titre du produit
    infos['title'] = affiche_texte_si_non_vide(bs.find('span',id='productTitle')) #str

    ratings_text = affiche_texte_si_non_vide(bs.find('span',id='customer-review-text'))
    if ratings_text:
        rnb_ratings_str = ratings_text.split()[0]
        if rnb_ratings_str.isdigit():
            infos['nb_ratings'] = int(rnb_ratings_str)

#extraction du price
    price_whole_str = affiche_texte_si_non_vide(bs.find('span',class_='price-whole'))
    price_fraction_str = affiche_texte_si_non_vide(bs.find('span',class_='price-fraction'))
    if price_whole_str and price_whole_str.isdigit():
        price = float(price_whole_str)
        if price_fraction_str and price_fraction_str.isdigit():
            price += (float(price_fraction_str) / 100)
        infos['price'] = price

#extraction de la description
    infos['descriptions'] = affiche_texte_si_non_vide(bs.find('div',id="product-description")) #str

    return infos    

data_to_save = {
    "titre_page": "Page TechSport",
    "url_source": "https://codeavecjonathan.com/scraping/techsport/",
    "contenu_html_extrait": "<html>...</html>", # Ici tu mettrais ton 'html_content' réel
    "date_extraction": "2025-07-24"
}

JSON_DATA_FILE = 'techsport.json'
DATE_TODAY = datetime.today()
DATE_TODAY_STR = DATE_TODAY.strftime('%d-%m-%y')

BYPASS = True
#fonction load

async def run(pw):

    try:
    # Ouvre le fichier en mode écriture ('w') avec l'encodage UTF-8
    # et utilise json.dump() pour écrire l'objet Python directement en JSON
    with open(JSON_DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    print(f"Les données ont été sauvegardées dans '{JSON_DATA_FILE}' avec succès.")

except Exception as e:
    print(f"Une erreur est survenue lors de l'écriture du fichier JSON : {e}")

    if not BYPASS:   
        print('Connecting to Browser API...') 
        browser = await pw.chromium.connect_over_cdp(SBR_WS_CDP)
    try:
        i = 0
        for url in URLS:
            i= i + 1
            print(f"page {i}/len{URLS}")

        if not BYPASS:    
            page = await browser.new_page()
            print('Connected! Navigating to webpage')
            await page.goto(url)
            await page.screenshot(path="page.png", full_page=True)
            print("Screenshot saved as 'page.png'")
            html = await page.content()
            print(html)

            with open('scraping-browser.html', 'w', encoding='utf-8') as f:
                f.write(html)
        else:
            print("le scraping n'est pas activé")
            with open('scraping-browser.html', 'r', encoding='utf-8') as f:
                html = f.read()

        #extraction des informations à partir du code html
        print('extraction en cours....')
        infos = extraction_product_page_infos(html)
        print(infos)

    finally:
        if not BYPASS:    
            await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

if __name__ == '__main__':
    asyncio.run(main())
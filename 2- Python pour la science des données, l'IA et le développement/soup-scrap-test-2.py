from typing import Text
import requests
from bs4 import BeautifulSoup

url = "https://codeavecjonathan.com/scraping/recette_ua/"
# url = "https://codeavecjonathan.com/scraping/techsport/"

HEADERS = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36'}

def affiche_texte_si_non_vide(texte):
    if texte:
        return texte.text.strip()
    return None

response = requests.get(url, headers = HEADERS)
response.encoding = response.apparent_encoding

print(f"fin du script")

if response.status_code == 200:
    html = response.text
    #print (html)

    f = open("recette.html", "w")
    f.write(html)
    f.close()

    soup = BeautifulSoup(html, 'html5lib')

    titre =  soup.find('h1').text
    print(titre)

    description = affiche_texte_si_non_vide(soup.find('p', class_= 'description'))
    print(description)

    #ingrédient
    div_ingredient = soup.find('div', class_='ingredients')
    e_ingredients = div_ingredient.find_all('p')
    for e_ingredient in e_ingredients:
        print('INGREDIENT',e_ingredient.text)

    #Etape de préparation
    table_prepration = soup.find('table', class_='preparation')
    e_etapes = table_prepration.find_all('td')
    for e_etape in e_etapes:
        print('ETAPE',e_etape.text)

else:
    print("ERREUR", response.status_code)

print (f"fin du script")
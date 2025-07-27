import urllib.request
import ssl

proxy = 'http://brd-customer-hl_9edf8c10-zone-datacenter_proxy1:ec92nopsadz6@brd.superproxy.io:33335'
url = 'https://codeavecjonathan.com/scraping/techsport/'

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'https': proxy, 'http': proxy}),
    urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
)

try:
    html_content = opener.open(url).read().decode()
    print(html_content)
    with open('web-unlocker.html', 'w', encoding='utf-8') as f:
        f.write(html_content) # Écrire le contenu HTML dans le fichier
except Exception as e:
    print(f"Error: {e}")
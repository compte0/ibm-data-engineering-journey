#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script principal de scraping pour emploi.cm
Extrait toutes les données des emplois et navigue à travers toutes les pages
Utilise le réseau de proxy résidentiel de Bright Data
"""

import requests
import json
import re
import time
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

class EmploiCMScraper:
    def __init__(self):
        """Initialisation du scraper avec configuration proxy"""
        self.base_url = "https://www.emploi.cm"
        self.search_url = "https://www.emploi.cm/recherche-jobs-cameroun"
        self.session = requests.Session()
        self.all_jobs = []
        self.total_jobs_scraped = 0
        
        # Configuration du proxy Bright Data
        self.setup_proxy()
        
        # Headers personnalisés
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 - Web Scraper Bot - Contact: chrisdavebenge@gmail.com - Purpose: Data Collection for Research',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Cache-Control': 'max-age=0',
        }
        
        self.session.headers.update(self.headers)
    
    def setup_proxy(self):
        """Configure le proxy Bright Data"""
        try:
            # Récupérer les informations de proxy depuis les variables d'environnement
            proxy_host = os.getenv('BRIGHT_DATA_PROXY_HOST')
            proxy_port = os.getenv('BRIGHT_DATA_PROXY_PORT')
            proxy_zone = os.getenv('BRIGHT_DATA_PROXY_ZONE')
            proxy_username = os.getenv('BRIGHT_DATA_PROXY_USERNAME')
            proxy_password = os.getenv('BRIGHT_DATA_PROXY_PASSWORD')
            
            if all([proxy_host, proxy_port, proxy_username, proxy_password]):
                # Configuration du proxy
                proxy_url = f"http://{proxy_username}-{proxy_zone}:{proxy_password}@{proxy_host}:{proxy_port}"
                self.proxies = {
                    'http': proxy_url,
                    'https': proxy_url
                }
                
                print(f"✅ Proxy Bright Data configuré")
                print(f"   Host: {proxy_host}:{proxy_port}")
                print(f"   Username: {proxy_username}")
                
                # Appliquer les proxies à la session
                self.session.proxies.update(self.proxies)
                
            else:
                print("⚠️  Variables d'environnement proxy manquantes, utilisation sans proxy")
                print("   Variables requises: BRIGHT_DATA_PROXY_HOST, BRIGHT_DATA_PROXY_PORT, BRIGHT_DATA_PROXY_USERNAME, BRIGHT_DATA_PROXY_PASSWORD")
                self.proxies = None
                
        except Exception as e:
            print(f"❌ Erreur lors de la configuration du proxy: {e}")
            print("   Utilisation sans proxy")
            self.proxies = None
    
    def get_page(self, url):
        """Récupère une page avec gestion d'erreurs"""
        try:
            print(f" Récupération de la page: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f" Erreur lors de la récupération de {url}: {e}")
            return None
    
    def extract_job_data(self, job_card):
        """Extrait les données d'une carte d'emploi (version filtrée - texte brut uniquement)"""
        try:
            job_data = {}
            
            # Titre du poste (texte brut)
            title_elem = job_card.find('h3')
            if title_elem:
                title_link = title_elem.find('a')
                if title_link:
                    job_data['titre'] = title_link.get('title', '').strip()
            
            # Entreprise (texte brut)
            company_elem = job_card.find('a', class_='card-job-company')
            if company_elem:
                job_data['entreprise'] = company_elem.get_text(strip=True)
            
            # Logo de l'entreprise (URL)
            logo_elem = job_card.find('img')
            if logo_elem:
                job_data['logo_entreprise'] = logo_elem.get('src', '')
            
            # Description (texte brut)
            desc_elem = job_card.find('div', class_='card-job-description')
            if desc_elem:
                desc_text = desc_elem.find('p')
                if desc_text:
                    job_data['description'] = desc_text.get_text(strip=True)
            
            # Détails spécifiques (texte brut)
            ul_elem = job_card.find('ul')
            if ul_elem:
                for li in ul_elem.find_all('li'):
                    text = li.get_text(strip=True)
                    if 'Niveau d´études requis' in text:
                        strong = li.find('strong')
                        if strong:
                            job_data['niveau_etudes'] = strong.get_text(strip=True)
                    elif 'Niveau d\'expérience' in text:
                        strong = li.find('strong')
                        if strong:
                            job_data['niveau_experience'] = strong.get_text(strip=True)
                    elif 'Contrat proposé' in text:
                        strong = li.find('strong')
                        if strong:
                            job_data['type_contrat'] = strong.get_text(strip=True)
                    elif 'Région de' in text:
                        strong = li.find('strong')
                        if strong:
                            job_data['region'] = strong.get_text(strip=True)
            
            # Date de publication
            time_elem = job_card.find('time')
            if time_elem:
                job_data['date_publication'] = time_elem.get('datetime', '')
            
            return job_data
            
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction des données d'un emploi: {e}")
            return None
    
    def extract_pagination_info(self, soup):
        """Extrait les informations de pagination"""
        pagination_info = {
            'current_page': 1,
            'total_pages': 1,
            'next_page_url': None
        }
        
        try:
            # Chercher la pagination
            pagination = soup.find('div', class_='pagination')
            if pagination:
                # Page courante
                current_elem = pagination.find('li', class_='pager-current')
                if current_elem:
                    pagination_info['current_page'] = int(current_elem.text.strip())
                
                # Pages totales (chercher le dernier lien de page)
                page_links = pagination.find_all('a')
                max_page = 1
                for link in page_links:
                    href = link.get('href', '')
                    if 'page=' in href:
                        page_match = re.search(r'page=(\d+)', href)
                        if page_match:
                            page_num = int(page_match.group(1))
                            if page_num > max_page:
                                max_page = page_num
                
                # Si on trouve des liens de page, le total est max_page + 1
                if max_page > 1:
                    pagination_info['total_pages'] = max_page + 1
                
                # URL de la page suivante
                next_elem = pagination.find('li', class_='pager-next')
                if next_elem:
                    next_link = next_elem.find('a')
                    if next_link:
                        pagination_info['next_page_url'] = urljoin(self.base_url, next_link.get('href', ''))
            
            print(f"📊 Pagination: Page {pagination_info['current_page']}/{pagination_info['total_pages']}")
            
        except Exception as e:
            print(f"❌ Erreur lors de l'extraction de la pagination: {e}")
        
        return pagination_info
    
    def scrape_page(self, url):
        """Scrape une page d'emplois"""
        html_content = self.get_page(url)
        if not html_content:
            return []
        
        soup = BeautifulSoup(html_content, 'html.parser')
        jobs_on_page = []
        
        # Chercher toutes les cartes d'emplois
        job_cards = soup.find_all('div', class_='card card-job')
        print(f"🔍 Trouvé {len(job_cards)} emplois sur cette page")
        
        for i, job_card in enumerate(job_cards, 1):
            print(f"  📋 Extraction de l'emploi {i}/{len(job_cards)}")
            job_data = self.extract_job_data(job_card)
            if job_data:
                jobs_on_page.append(job_data)
                self.total_jobs_scraped += 1
        
        return jobs_on_page
    
    def scrape_all_pages(self):
        """Scrape toutes les pages d'emplois"""
        print("🚀 Début du scraping complet d'emploi.cm")
        print("=" * 60)
        
        current_url = self.search_url
        page_num = 1
        
        while current_url:
            print(f"\n📄 PAGE {page_num}")
            print("-" * 40)
            
            # Scraper la page courante
            jobs_on_page = self.scrape_page(current_url)
            self.all_jobs.extend(jobs_on_page)
            
            print(f"✅ {len(jobs_on_page)} emplois extraits de la page {page_num}")
            print(f"📊 Total cumulé: {self.total_jobs_scraped} emplois")
            
            # Récupérer les informations de pagination
            html_content = self.get_page(current_url)
            if html_content:
                soup = BeautifulSoup(html_content, 'html.parser')
                pagination_info = self.extract_pagination_info(soup)
                
                # Vérifier s'il y a une page suivante
                if pagination_info['next_page_url'] and page_num < pagination_info['total_pages']:
                    current_url = pagination_info['next_page_url']
                    page_num += 1
                    print(f"⏭️  Passage à la page suivante: {current_url}")
                    
                    # Pause pour éviter de surcharger le serveur
                    time.sleep(2)
                else:
                    print("🏁 Fin des pages atteinte")
                    break
            else:
                print("❌ Impossible de récupérer la page pour la pagination")
                break
        
        print(f"\n🎉 Scraping terminé! Total: {self.total_jobs_scraped} emplois extraits")
    
    def save_to_json(self, filename=None):
        """Sauvegarde les données en JSON"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"emplois_cameroun_{timestamp}.json"
        
        data = {
            'metadata': {
                'source': 'emploi.cm',
                'date_scraping': datetime.now().isoformat(),
                'total_emplois': len(self.all_jobs),
                'contact': 'chrisdavebenge@gmail.com',
                'description': 'Données extraites du site emploi.cm'
            },
            'emplois': self.all_jobs
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"💾 Données sauvegardées dans: {filename}")
            print(f"📊 {len(self.all_jobs)} emplois sauvegardés")
            
            # Afficher quelques statistiques
            self.show_statistics()
            
        except Exception as e:
            print(f"❌ Erreur lors de la sauvegarde: {e}")
    
    def show_statistics(self):
        """Affiche des statistiques sur les données récupérées"""
        if not self.all_jobs:
            print("❌ Aucune donnée à analyser")
            return
        
        print("\n📈 STATISTIQUES")
        print("=" * 40)
        
        # Statistiques par région
        regions = {}
        for job in self.all_jobs:
            region = job.get('region', 'Non spécifiée')
            regions[region] = regions.get(region, 0) + 1
        
        print("🌍 Emplois par région:")
        for region, count in sorted(regions.items(), key=lambda x: x[1], reverse=True):
            print(f"  {region}: {count}")
        
        # Statistiques par type de contrat
        contrats = {}
        for job in self.all_jobs:
            contrat = job.get('type_contrat', 'Non spécifié')
            contrats[contrat] = contrats.get(contrat, 0) + 1
        
        print("\n📋 Emplois par type de contrat:")
        for contrat, count in sorted(contrats.items(), key=lambda x: x[1], reverse=True):
            print(f"  {contrat}: {count}")
        
        # Top entreprises
        entreprises = {}
        for job in self.all_jobs:
            entreprise = job.get('entreprise', 'Non spécifiée')
            entreprises[entreprise] = entreprises.get(entreprise, 0) + 1
        
        print("\n🏢 Top 10 entreprises recrutant:")
        for entreprise, count in sorted(entreprises.items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"  {entreprise}: {count}")
        
        # Statistiques par niveau d'études
        niveaux = {}
        for job in self.all_jobs:
            niveau = job.get('niveau_etudes', 'Non spécifié')
            niveaux[niveau] = niveaux.get(niveau, 0) + 1
        
        print("\n🎓 Emplois par niveau d'études:")
        for niveau, count in sorted(niveaux.items(), key=lambda x: x[1], reverse=True):
            print(f"  {niveau}: {count}")
        
        # Statistiques par niveau d'expérience
        experiences = {}
        for job in self.all_jobs:
            exp = job.get('niveau_experience', 'Non spécifié')
            experiences[exp] = experiences.get(exp, 0) + 1
        
        print("\n💼 Emplois par niveau d'expérience:")
        for exp, count in sorted(experiences.items(), key=lambda x: x[1], reverse=True):
            print(f"  {exp}: {count}")
        
        # Emplois avec description
        emplois_avec_desc = sum(1 for e in self.all_jobs if e.get('description'))
        print(f"\n📝 Emplois avec description: {emplois_avec_desc}/{len(self.all_jobs)}")
        
        # Emplois avec logo
        emplois_avec_logo = sum(1 for e in self.all_jobs if e.get('logo_entreprise'))
        print(f"🖼️  Emplois avec logo: {emplois_avec_logo}/{len(self.all_jobs)}")

def main():
    """Fonction principale"""
    print("🔍 Scraper emploi.cm - Extraction complète des emplois")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 60)
    
    # Créer le scraper
    scraper = EmploiCMScraper()
    
    # Lancer le scraping complet
    scraper.scrape_all_pages()
    
    # Sauvegarder les données
    if scraper.all_jobs:
        scraper.save_to_json()
    else:
        print("❌ Aucun emploi n'a été récupéré")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration pour le scraper emploi.cm
"""

# Configuration de l'URL
TARGET_URL = "https://www.emploi.cm/recherche-jobs-cameroun"

# Configuration des headers HTTP
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 - Web Scraper Bot - Contact: chrisdavebenge@gmail.com - Purpose: Data Collection for Research',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Accept-Encoding': 'gzip, deflate',  # Évite la compression Brotli
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Cache-Control': 'max-age=0',
}

# Configuration des timeouts
TIMEOUT = 30

# Configuration des fichiers
FILE_PREFIX = "emploi_cm_recherche"
FILE_EXTENSION = ".html"

# Configuration du contact
CONTACT_EMAIL = "chrisdavebenge@gmail.com"

# Configuration des logs
VERBOSE = True

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour le scraper emploi.cm
"""

import os
import sys
from datetime import datetime

def test_environment():
    """Test de l'environnement Python et des dépendances"""
    print("=== Test de l'environnement ===")
    
    # Test Python
    print(f"Python version: {sys.version}")
    
    # Test des imports
    try:
        import requests
        print(f"✅ Requests version: {requests.__version__}")
    except ImportError:
        print("❌ Requests non installé")
        return False
    
    try:
        import brotli
        print(f"✅ Brotli installé")
    except ImportError:
        print("❌ Brotli non installé")
        return False
    
    return True

def test_scraper():
    """Test du scraper principal"""
    print("\n=== Test du scraper ===")
    
    try:
        from scraper import scrape_emploi_cm
        print("✅ Import du scraper réussi")
        
        # Test de la fonction
        result = scrape_emploi_cm()
        if result:
            print("✅ Scraping réussi")
            return True
        else:
            print("❌ Échec du scraping")
            return False
            
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        return False

def check_files():
    """Vérification des fichiers créés"""
    print("\n=== Vérification des fichiers ===")
    
    # Vérifier les fichiers HTML
    html_files = [f for f in os.listdir('.') if f.endswith('.html') and 'emploi_cm' in f]
    
    if html_files:
        print(f"✅ {len(html_files)} fichier(s) HTML trouvé(s):")
        for file in sorted(html_files, reverse=True)[:3]:  # Afficher les 3 plus récents
            size = os.path.getsize(file)
            print(f"   - {file} ({size:,} bytes)")
    else:
        print("❌ Aucun fichier HTML trouvé")
        return False
    
    return True

def main():
    """Fonction principale de test"""
    print("🧪 Test du Scraper emploi.cm")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 50)
    
    # Tests
    env_ok = test_environment()
    if not env_ok:
        print("\n❌ Environnement non configuré correctement")
        return
    
    scraper_ok = test_scraper()
    if not scraper_ok:
        print("\n❌ Le scraper ne fonctionne pas correctement")
        return
    
    files_ok = check_files()
    if not files_ok:
        print("\n❌ Problème avec les fichiers créés")
        return
    
    print("\n🎉 Tous les tests sont passés avec succès!")
    print("Le scraper est prêt à être utilisé.")

if __name__ == "__main__":
    main()

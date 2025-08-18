#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour vérifier la configuration du proxy Bright Data
"""

import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

def test_proxy_configuration():
    """Teste la configuration du proxy"""
    print("🔧 Test de la configuration du proxy Bright Data")
    print("=" * 60)
    
    # Vérifier les variables d'environnement
    proxy_host = os.getenv('BRIGHT_DATA_PROXY_HOST')
    proxy_port = os.getenv('BRIGHT_DATA_PROXY_PORT')
    proxy_username = os.getenv('BRIGHT_DATA_PROXY_USERNAME')
    proxy_password = os.getenv('BRIGHT_DATA_PROXY_PASSWORD')
    
    print("📋 Variables d'environnement:")
    print(f"  - BRIGHT_DATA_PROXY_HOST: {'✅' if proxy_host else '❌'} {proxy_host or 'Non défini'}")
    print(f"  - BRIGHT_DATA_PROXY_PORT: {'✅' if proxy_port else '❌'} {proxy_port or 'Non défini'}")
    print(f"  - BRIGHT_DATA_PROXY_USERNAME: {'✅' if proxy_username else '❌'} {proxy_username or 'Non défini'}")
    print(f"  - BRIGHT_DATA_PROXY_PASSWORD: {'✅' if proxy_password else '❌'} {'***' if proxy_password else 'Non défini'}")
    
    if not all([proxy_host, proxy_port, proxy_username, proxy_password]):
        print("\n❌ Configuration incomplète!")
        print("   Assurez-vous que toutes les variables d'environnement sont définies dans le fichier .env")
        return False
    
    # Configuration du proxy
    proxy_url = f"http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
    proxies = {
        'http': proxy_url,
        'https': proxy_url
    }
    
    print(f"\n🔗 URL du proxy: {proxy_url}")
    
    # Test de connexion
    print("\n🌐 Test de connexion...")
    try:
        # Test avec un service qui affiche l'IP
        test_url = "http://httpbin.org/ip"
        
        print(f"   Test de connexion à: {test_url}")
        
        response = requests.get(test_url, proxies=proxies, timeout=30)
        response.raise_for_status()
        
        ip_info = response.json()
        print(f"   ✅ Connexion réussie!")
        print(f"   📍 IP détectée: {ip_info.get('origin', 'N/A')}")
        
        return True
        
    except requests.exceptions.ProxyError as e:
        print(f"   ❌ Erreur de proxy: {e}")
        return False
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Erreur de connexion: {e}")
        return False
    except Exception as e:
        print(f"   ❌ Erreur inattendue: {e}")
        return False

def test_with_session():
    """Test avec une session requests (comme dans le scraper)"""
    print("\n🔧 Test avec session requests (simulation du scraper)")
    print("-" * 50)
    
    try:
        from main import EmploiCMScraper
        
        # Créer une instance du scraper
        scraper = EmploiCMScraper()
        
        # Test de connexion avec la session configurée
        test_url = "http://httpbin.org/ip"
        print(f"   Test avec session à: {test_url}")
        
        response = scraper.session.get(test_url, timeout=30)
        response.raise_for_status()
        
        ip_info = response.json()
        print(f"   ✅ Session configurée avec succès!")
        print(f"   📍 IP détectée: {ip_info.get('origin', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Erreur avec la session: {e}")
        return False

def main():
    """Fonction principale"""
    print("🧪 Test de la configuration du proxy Bright Data")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 60)
    
    # Test de la configuration
    config_ok = test_proxy_configuration()
    
    if config_ok:
        # Test avec session
        session_ok = test_with_session()
        
        if session_ok:
            print("\n🎉 Tous les tests sont passés!")
            print("   Le proxy est correctement configuré et fonctionnel.")
        else:
            print("\n⚠️  Configuration OK mais problème avec la session.")
    else:
        print("\n❌ Configuration du proxy incorrecte.")
        print("   Vérifiez votre fichier .env et vos informations Bright Data.")

if __name__ == "__main__":
    main()

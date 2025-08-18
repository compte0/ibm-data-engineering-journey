#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour analyser le fichier JSON filtré
"""

import json
import os
from datetime import datetime

def analyze_filtered_json(filename):
    """Analyse le fichier JSON filtré"""
    print(f"🔍 Analyse du fichier filtré: {filename}")
    print("=" * 60)
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Informations sur les métadonnées
        metadata = data.get('metadata', {})
        print(f"📊 Métadonnées:")
        print(f"  - Source: {metadata.get('source', 'N/A')}")
        print(f"  - Date de scraping: {metadata.get('date_scraping', 'N/A')}")
        print(f"  - Total d'emplois: {metadata.get('total_emplois', 'N/A')}")
        print(f"  - Contact: {metadata.get('contact', 'N/A')}")
        
        # Informations sur les emplois
        emplois = data.get('emplois', [])
        print(f"\n📋 Informations sur les emplois:")
        print(f"  - Nombre d'emplois: {len(emplois)}")
        
        if emplois:
            # Analyser le premier emploi pour voir la structure
            premier_emploi = emplois[0]
            print(f"\n🔍 Structure du premier emploi (champs filtrés):")
            for key, value in premier_emploi.items():
                print(f"  - {key}: {type(value).__name__}")
                if isinstance(value, str) and len(value) > 50:
                    print(f"    Contenu: {value[:50]}...")
                else:
                    print(f"    Contenu: {value}")
            
            # Vérifier que tous les champs requis sont présents
            champs_requis = [
                'titre', 'entreprise', 'logo_entreprise', 'description',
                'niveau_etudes', 'niveau_experience', 'type_contrat',
                'region', 'date_publication'
            ]
            
            print(f"\n✅ Vérification des champs requis:")
            for champ in champs_requis:
                emplois_avec_champ = sum(1 for e in emplois if e.get(champ))
                print(f"  - {champ}: {emplois_avec_champ}/{len(emplois)} emplois")
            
            # Statistiques sur la qualité des données
            print(f"\n📈 Qualité des données:")
            
            # Emplois avec description complète
            emplois_avec_desc = sum(1 for e in emplois if e.get('description') and len(e['description']) > 50)
            print(f"  - Emplois avec description complète: {emplois_avec_desc}/{len(emplois)}")
            
            # Emplois avec logo personnalisé (pas le logo par défaut)
            emplois_avec_logo_perso = sum(1 for e in emplois if e.get('logo_entreprise') and 'default-logo' not in e['logo_entreprise'])
            print(f"  - Emplois avec logo personnalisé: {emplois_avec_logo_perso}/{len(emplois)}")
            
            # Emplois récents (moins de 30 jours)
            from datetime import datetime, timedelta
            date_limite = datetime.now() - timedelta(days=30)
            emplois_recents = 0
            for e in emplois:
                if e.get('date_publication'):
                    try:
                        date_pub = datetime.strptime(e['date_publication'], '%Y-%m-%d')
                        if date_pub >= date_limite:
                            emplois_recents += 1
                    except:
                        pass
            print(f"  - Emplois récents (< 30 jours): {emplois_recents}/{len(emplois)}")
        
        print(f"\n✅ Analyse terminée avec succès!")
        
    except FileNotFoundError:
        print(f"❌ Fichier {filename} non trouvé")
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de décodage JSON: {e}")
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {e}")

def find_latest_filtered_json():
    """Trouve le fichier JSON filtré le plus récent"""
    json_files = [f for f in os.listdir('.') if f.endswith('.json') and 'emplois_cameroun' in f and 'filtre' not in f]
    
    if not json_files:
        print("❌ Aucun fichier JSON d'emplois trouvé")
        return None
    
    # Trier par date de modification
    latest_file = max(json_files, key=lambda f: os.path.getmtime(f))
    return latest_file

def main():
    """Fonction principale"""
    print("🧪 Test du fichier JSON filtré")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 60)
    
    # Trouver le fichier JSON le plus récent
    json_file = find_latest_filtered_json()
    
    if json_file:
        print(f"📁 Fichier trouvé: {json_file}")
        
        # Informations sur le fichier
        file_size = os.path.getsize(json_file)
        file_time = datetime.fromtimestamp(os.path.getmtime(json_file))
        
        print(f"📊 Taille du fichier: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print(f"📅 Date de modification: {file_time}")
        
        # Analyser le contenu
        analyze_filtered_json(json_file)
    else:
        print("❌ Aucun fichier JSON à analyser")

if __name__ == "__main__":
    main()

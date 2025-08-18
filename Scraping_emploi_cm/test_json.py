#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour analyser le fichier JSON généré
"""

import json
import os
from datetime import datetime

def analyze_json_file(filename):
    """Analyse le fichier JSON généré"""
    print(f"🔍 Analyse du fichier: {filename}")
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
            print(f"\n🔍 Structure du premier emploi:")
            for key, value in premier_emploi.items():
                if isinstance(value, dict):
                    print(f"  - {key}: {type(value).__name__} avec {len(value)} clés")
                    for sub_key, sub_value in value.items():
                        print(f"    * {sub_key}: {type(sub_value).__name__}")
                else:
                    print(f"  - {key}: {type(value).__name__}")
            
            # Statistiques détaillées
            print(f"\n📈 Statistiques détaillées:")
            
            # Régions
            regions = {}
            for emploi in emplois:
                region = emploi.get('details', {}).get('region', 'Non spécifiée')
                regions[region] = regions.get(region, 0) + 1
            
            print(f"  - Nombre de régions différentes: {len(regions)}")
            
            # Entreprises
            entreprises = {}
            for emploi in emplois:
                entreprise = emploi.get('entreprise', 'Non spécifiée')
                entreprises[entreprise] = entreprises.get(entreprise, 0) + 1
            
            print(f"  - Nombre d'entreprises différentes: {len(entreprises)}")
            
            # Types de contrat
            contrats = {}
            for emploi in emplois:
                contrat = emploi.get('details', {}).get('type_contrat', 'Non spécifié')
                contrats[contrat] = contrats.get(contrat, 0) + 1
            
            print(f"  - Nombre de types de contrat différents: {len(contrats)}")
            
            # Emplois avec description
            emplois_avec_desc = sum(1 for e in emplois if e.get('description'))
            print(f"  - Emplois avec description: {emplois_avec_desc}/{len(emplois)}")
            
            # Emplois avec logo
            emplois_avec_logo = sum(1 for e in emplois if e.get('logo_entreprise'))
            print(f"  - Emplois avec logo: {emplois_avec_logo}/{len(emplois)}")
            
            # Emplois avec ID
            emplois_avec_id = sum(1 for e in emplois if e.get('id_offre'))
            print(f"  - Emplois avec ID: {emplois_avec_id}/{len(emplois)}")
        
        print(f"\n✅ Analyse terminée avec succès!")
        
    except FileNotFoundError:
        print(f"❌ Fichier {filename} non trouvé")
    except json.JSONDecodeError as e:
        print(f"❌ Erreur de décodage JSON: {e}")
    except Exception as e:
        print(f"❌ Erreur lors de l'analyse: {e}")

def find_latest_json():
    """Trouve le fichier JSON le plus récent"""
    json_files = [f for f in os.listdir('.') if f.endswith('.json') and 'emplois_cameroun' in f]
    
    if not json_files:
        print("❌ Aucun fichier JSON d'emplois trouvé")
        return None
    
    # Trier par date de modification
    latest_file = max(json_files, key=lambda f: os.path.getmtime(f))
    return latest_file

def main():
    """Fonction principale"""
    print("🧪 Test du fichier JSON généré")
    print("Contact: chrisdavebenge@gmail.com")
    print("=" * 60)
    
    # Trouver le fichier JSON le plus récent
    json_file = find_latest_json()
    
    if json_file:
        print(f"📁 Fichier trouvé: {json_file}")
        
        # Informations sur le fichier
        file_size = os.path.getsize(json_file)
        file_time = datetime.fromtimestamp(os.path.getmtime(json_file))
        
        print(f"📊 Taille du fichier: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        print(f"📅 Date de modification: {file_time}")
        
        # Analyser le contenu
        analyze_json_file(json_file)
    else:
        print("❌ Aucun fichier JSON à analyser")

if __name__ == "__main__":
    main()

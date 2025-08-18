# Scraper emploi.cm

Script de scraping pour récupérer les données de la page de recherche d'emplois du site emploi.cm.

##  Objectif

Ce projet permet de récupérer automatiquement le contenu HTML de la page de recherche d'emplois du site emploi.cm (https://www.emploi.cm/recherche-jobs-cameroun) et de le sauvegarder localement pour analyse.

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. **Cloner ou télécharger le projet** dans un dossier local

2. **Créer l'environnement virtuel** :
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel** :
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (Command Prompt)
venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

4. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

## Utilisation

### Script principal (extraction complète)
```bash
python main.py
```

### Script de scraping simple
```bash
python scraper.py
```

### Tests et analyses
```bash
# Test de l'environnement
python test_scraper.py

# Analyse du fichier JSON complet
python test_json.py

# Analyse du fichier JSON filtré
python test_json_filtre.py
```

## 📁 Structure du projet

```
scraping_emploi_cm/
├── main.py              # Script principal (extraction complète + pagination)
├── scraper.py           # Script de scraping simple (une page)
├── test_scraper.py      # Test de l'environnement
├── test_json.py         # Analyse du JSON complet
├── test_json_filtre.py  # Analyse du JSON filtré
├── config.py            # Configuration centralisée
├── requirements.txt     # Dépendances Python
├── README.md           # Documentation
├── venv/               # Environnement virtuel
└── *.json              # Fichiers JSON récupérés
```

## Configuration

Le fichier `config.py` contient tous les paramètres configurables :

- **URL cible** : Page de recherche d'emplois
- **Headers HTTP** : User-Agent personnalisé avec contact
- **Timeouts** : Délais de connexion
- **Format des fichiers** : Préfixe et extension des fichiers sauvegardés

## Fonctionnalités

### Fonctionnalités implémentées

- **Scraping automatique** de la page de recherche d'emplois
- **Navigation automatique** à travers toutes les pages (pagination)
- **Extraction filtrée** des données essentielles uniquement
- **User-Agent personnalisé** avec informations de contact
- **Gestion de la compression** (gzip, Brotli)
- **Sauvegarde automatique** avec timestamp
- **Gestion d'erreurs** robuste
- **Logs détaillés** pour le debugging
- **Tests automatisés** de l'environnement
- **Statistiques détaillées** sur les données récupérées

### 🎯 Données extraites (version filtrée)

Le script `main.py` extrait uniquement les données essentielles :

- **titre** : Titre du poste
- **entreprise** : Nom de l'entreprise
- **logo_entreprise** : URL du logo de l'entreprise
- **description** : Description du poste (texte brut)
- **niveau_etudes** : Niveau d'études requis
- **niveau_experience** : Niveau d'expérience requis
- **type_contrat** : Type de contrat proposé
- **region** : Région du poste
- **date_publication** : Date de publication

### 🛡️ Bonnes pratiques respectées

- **Respect des robots.txt** (User-Agent approprié)
- **Informations de contact** incluses
- **Timeouts appropriés** pour éviter la surcharge
- **Headers HTTP complets** pour éviter la détection
- **Gestion des encodages** et compressions
- **Pauses entre les requêtes** pour éviter la surcharge

## Exemple de sortie

```
🚀 Début du scraping complet d'emploi.cm
============================================================

📄 PAGE 1
📄 Récupération de la page: https://www.emploi.cm/recherche-jobs-cameroun
🔍 Trouvé 25 emplois sur cette page
✅ 25 emplois extraits de la page 1
📊 Total cumulé: 25 emplois

📄 PAGE 2
...
🎉 Scraping terminé! Total: 231 emplois extraits
💾 Données sauvegardées dans: emplois_cameroun_20250818_005916.json
📊 231 emplois sauvegardés

📈 STATISTIQUES
🌍 Emplois par région:
  Douala: 79
  Yaoundé: 67
  ...

📋 Emplois par type de contrat:
  CDI: 72
  CDD: 35
  ...

🏢 Top 10 entreprises recrutant:
  AFRICASHORE: 42
  SASA B2E: 17
  ...
```

## 📧 Contact

Pour toute question concernant ce scraper, contactez : **chrisdavebenge@gmail.com**

## ⚠️ Avertissements

- Ce script est destiné à un usage éducatif et de recherche
- Respectez les conditions d'utilisation du site cible
- N'utilisez pas ce script de manière abusive
- Les données récupérées sont à utiliser conformément aux lois en vigueur

## 🔄 Mise à jour

Pour mettre à jour les dépendances :
```bash
pip install --upgrade -r requirements.txt
```

## 📄 Licence

Ce projet est fourni à des fins éducatives. Utilisez-le de manière responsable.


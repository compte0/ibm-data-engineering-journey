# Guide de configuration du proxy Bright Data

Ce guide vous explique comment configurer le réseau de proxy résidentiel de Bright Data avec le scraper emploi.cm.

## 📋 Prérequis

- Compte Bright Data avec accès au réseau de proxy résidentiel
- Informations de connexion proxy (host, port, username, password)

## 🔧 Configuration

### 1. Créer le fichier .env

Créez un fichier `.env` à la racine du projet avec les informations suivantes :

```env
# Configuration Bright Data Proxy
BRIGHT_DATA_PROXY_HOST=brd.superproxy.io
BRIGHT_DATA_PROXY_PORT=22225
BRIGHT_DATA_PROXY_USERNAME=brd-customer-zone-residential-username
BRIGHT_DATA_PROXY_PASSWORD=votre_mot_de_passe
```

### 2. Variables d'environnement requises

| Variable | Description | Exemple |
|----------|-------------|---------|
| `BRIGHT_DATA_PROXY_HOST` | Host du proxy Bright Data | `brd.superproxy.io` |
| `BRIGHT_DATA_PROXY_PORT` | Port du proxy (généralement 22225) | `22225` |
| `BRIGHT_DATA_PROXY_USERNAME` | Nom d'utilisateur Bright Data | `brd-customer-zone-residential-username` |
| `BRIGHT_DATA_PROXY_PASSWORD` | Mot de passe Bright Data | `votre_mot_de_passe` |

### 3. Où trouver vos informations Bright Data

1. Connectez-vous à votre dashboard Bright Data
2. Allez dans la section "Residential Proxies"
3. Cliquez sur "Configure"
4. Copiez les informations de connexion

## 🧪 Test de la configuration

### Test rapide
```bash
python test_proxy.py
```

Ce script vérifie :
- ✅ Présence des variables d'environnement
- ✅ Configuration du proxy
- ✅ Test de connexion
- ✅ Test avec la session du scraper

### Sortie attendue
```
✅ Proxy Bright Data configuré
   Host: brd.superproxy.io:22225
   Username: brd-customer-zone-residential-username

🌐 Test de connexion...
   Test de connexion à: http://httpbin.org/ip
   ✅ Connexion réussie!
   📍 IP détectée: 123.45.67.89

🎉 Tous les tests sont passés!
   Le proxy est correctement configuré et fonctionnel.
```

## 🚀 Utilisation

### Avec proxy configuré
```bash
python main.py
```

Le script affichera :
```
✅ Proxy Bright Data configuré
   Host: brd.superproxy.io:22225
   Username: brd-customer-zone-residential-username

🚀 Début du scraping complet d'emploi.cm
...
```

### Sans proxy configuré
```bash
python main.py
```

Le script affichera :
```
⚠️  Variables d'environnement proxy manquantes, utilisation sans proxy
   Variables requises: BRIGHT_DATA_PROXY_HOST, BRIGHT_DATA_PROXY_PORT, BRIGHT_DATA_PROXY_USERNAME, BRIGHT_DATA_PROXY_PASSWORD

🚀 Début du scraping complet d'emploi.cm
...
```

## 🔒 Sécurité

### Protection du fichier .env
- Ne committez jamais le fichier `.env` dans Git
- Le fichier `.env` est déjà dans `.gitignore`
- Gardez vos informations de proxy confidentielles

### Variables d'environnement alternatives
Vous pouvez aussi définir les variables d'environnement directement dans votre système :

**Windows (PowerShell) :**
```powershell
$env:BRIGHT_DATA_PROXY_HOST="brd.superproxy.io"
$env:BRIGHT_DATA_PROXY_PORT="22225"
$env:BRIGHT_DATA_PROXY_USERNAME="brd-customer-zone-residential-username"
$env:BRIGHT_DATA_PROXY_PASSWORD="votre_mot_de_passe"
```

**Linux/Mac :**
```bash
export BRIGHT_DATA_PROXY_HOST="brd.superproxy.io"
export BRIGHT_DATA_PROXY_PORT="22225"
export BRIGHT_DATA_PROXY_USERNAME="brd-customer-zone-residential-username"
export BRIGHT_DATA_PROXY_PASSWORD="votre_mot_de_passe"
```

## 🛠️ Dépannage

### Erreur : "Variables d'environnement proxy manquantes"
**Solution :** Vérifiez que le fichier `.env` existe et contient toutes les variables requises.

### Erreur : "Erreur de proxy"
**Solutions possibles :**
1. Vérifiez vos informations de connexion Bright Data
2. Assurez-vous que votre compte Bright Data est actif
3. Vérifiez que vous avez des crédits disponibles
4. Testez avec un autre port si nécessaire

### Erreur : "Timeout"
**Solutions possibles :**
1. Augmentez le timeout dans le script
2. Vérifiez votre connexion internet
3. Essayez avec un autre proxy du réseau

## 📞 Support

Pour toute question concernant ce scraper, contactez : **chrisdavebenge@gmail.com**

Pour le support Bright Data, consultez leur documentation officielle.

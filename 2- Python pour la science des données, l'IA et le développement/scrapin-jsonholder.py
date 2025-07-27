import requests

# URL du point de terminaison (endpoint) pour récupérer tous les posts
url = "https://jsonplaceholder.typicode.com/posts"

# 1. Faire une requête GET pour récupérer tous les posts
try:
    response = requests.get(url)

    # Vérifier si la requête a réussi (code 200 OK)
    response.raise_for_status()  # Lève une exception pour les codes d'erreur HTTP (4xx ou 5xx)

    # Convertir la réponse JSON en objet Python (liste de dictionnaires)
    posts = response.json()

    print(f"Nombre de posts récupérés : {len(posts)}")
    print("\nInformations sur le premier post :")
    print(f"ID : {posts[0]['id']}")
    print(f"Titre : {posts[0]['title']}")
    print(f"Corps : {posts[0]['body'][:50]}...") # Affiche les 50 premiers caractères

    # 2. Faire une requête GET pour un post spécifique (par exemple, le post avec l'ID 1)
    url_specific_post = f"{url}/1"
    response_specific = requests.get(url_specific_post)
    response_specific.raise_for_status()
    specific_post = response_specific.json()

    print("\nInformations sur le post avec l'ID 1 :")
    print(f"Titre : {specific_post['title']}")

    # 3. Faire une requête POST pour créer un nouveau post
    new_post_data = {
        "title": "Mon Super Nouveau Post",
        "body": "Ceci est le contenu de mon nouveau post génial.",
        "userId": 1
    }
    response_post = requests.post(url, json=new_post_data) # 'json' pour envoyer des données JSON
    response_post.raise_for_status()

    created_post = response_post.json()
    print("\nNouveau post créé (simulé) :")
    print(f"ID attribué (par l'API) : {created_post['id']}")
    print(f"Titre : {created_post['title']}")
    print(f"Statut HTTP : {response_post.status_code}") # Devrait être 201 Created

except requests.exceptions.HTTPError as err:
    print(f"Erreur HTTP : {err}")
except requests.exceptions.RequestException as err:
    print(f"Erreur de requête : {err}")
'''code 1'''
#création de dictionnaire
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}
print(f"Dictionnaire 'personne' initial : {personne}")

# Accéder à la valeur associée à la clé "nom"
nom_personne = personne.get("nom")
pays_personne = personne.get("ville")

#affichage des valeurs
print(f"{nom_personne} est originaire de la ville de {pays_personne}")

# Ajout d'une nouvelle clé-valeur
personne["email"] = "alice@example.com"
print(f"Après ajout de l'email : {personne}")

personne["profession"] = "Développeur"
print(f"Après ajout de la profession : {personne}")

personne["Origine"] = "caucasien"
print(f"le nouveau dictionnaire est {personne}")

'''code 2'''
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}
print(f"Dictionnaire 'personne' initial : {personne}")

# Modification de la valeur de la clé "age"
personne["age"] = 31
print(f"Après modification de l'âge : {personne}")

# Modification de la valeur de la clé "ville"
personne["ville"] = "Lyon"
print(f"Après modification de la ville : {personne}")

#suppression de clé
del personne ["sexe"]

'''code 3'''
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris",
    "email": "alice@example.com"
}
print(f"Dictionnaire 'personne' initial : {personne}")

# Suppression avec del
del personne["email"]
print(f"Après suppression de l'email (del) : {personne}\n")

# Suppression avec pop()
age_supprime = personne.pop("age")
print(f"Après suppression de l'âge (pop) : {personne}")
print(f"Âge supprimé : {age_supprime}\n")

# Suppression avec pop() et valeur par défaut
profession = personne.pop("profession", "Inconnu")
print(f"Après tentative de suppression d'une clé inexistante (pop avec défaut) : {personne}")
print(f"Profession : {profession}\n")

# Ajout d'éléments pour popitem()
personne["pays"] = "France"
personne["code_postal"] = "75001"
print(f"Dictionnaire avant popitem : {personne}")

# Suppression avec popitem()
dernier_element_supprime = personne.popitem()
print(f"Après suppression du dernier élément (popitem) : {personne}")
print(f"Dernier élément supprimé : {dernier_element_supprime}\n")

# Vider le dictionnaire avec clear()
#personne.clear()
#print(f"Après avoir vidé le dictionnaire (clear) : {personne}")

#ressortir toute les clés
personne_cles = list(personne.keys())


'''code 4'''
fruits = {
    "pomme": 1.50,
    "banane": 0.75,
    "orange": 1.20
}

cles = fruits.keys()
print(f"Clés des fruits : {cles}")

# Vous pouvez le convertir en liste si nécessaire
liste_cles = list(cles)
print(f"Liste des clés : {liste_cles}")


'''code 5'''
#création de la bibliothèque
livre = {
    "titre" : "Le Petit Prince",
    "auteur" : "Antoine de Saint-Exupéry",
    "annee_publication" : 1943,
    "genre" : "Conte philosophique"
}

print(f"Voici le contenu total de notre bibliothèque {livre}")

#accédons et affichagons le titre et le nom de l'auteur du livre
titre_get = livre.get("titre")
auteur_get = livre.get("auteur")
page_get = livre.get("page", "Non disponible")
print(f"l'auteur du livre; {titre_get} dans ce dictionnaire est: {auteur_get}")
print(f"le nombre de pages du livre est de: {page_get}")

#modification de l'année de publication
livre["annee_publication"] = "1944"

#ajout d'une nouvelle clé-valeur
livre["langue"] = "Français"

#affichage du nouveau dictionnaire
print(f"notre nouveau dictionnaire est: {livre}")

#suppresion du genre et affichage du dictionnaire
del livre["genre"]
print(f"notre nouveau dictionnaire est: {livre}")

#affichage des clé et valeurs du dictionnaire
cles = list(livre.keys())
valeurs = list(livre.values())
print(f"Voici la liste regroupant toute les clés du dictionnaire: {cles}")
print(f"Voici la liste regroupant toute les valeurs du dictionnaire: {valeurs}")


'''code 6'''
#construction des dictionnaire
inventaire_magasin = {
    "Electronique": {
        "Telephone": {"prix": 800,
                      "quantite": 50},
        "Ordinateur": {"prix": 1200,
                       "quantite": 30}
    },
    "Vetements": {
        "T-shirt": {"prix": 20,
                    "quantite": 200},
        "Jean": {"prix": 60,
                 "quantite": 100}
    }
}

#Affichez le prix de l'ordinateur.

prix_pc = Ordinateur.get[ordinateur][ordinateur][prix]

'''code 7'''
# Créez le dictionnaire inventaire_magasin
inventaire_magasin = {
    "Électronique": {
        "Téléphone": {"prix": 800, "quantite": 50},
        "Ordinateur": {"prix": 1200, "quantite": 30}
    },
    "Vêtements": {
        "T-shirt": {"prix": 20, "quantite": 200},
        "Jean": {"prix": 60, "quantite": 100}
    }
}

print(f"Inventaire initial :{inventaire_magasin}")
print("-" * 30)

# Affichez le prix de l'ordinateur.
prix_ordinateur = inventaire_magasin["Électronique"]["Ordinateur"]["prix"]
print(f"Le prix de l'ordinateur est : {prix_ordinateur}€")
print("-" * 30)

# Ajoutez un nouvel article "Casque" dans la catégorie "Électronique"
# avec un prix de 150 et une quantité de 75.
inventaire_magasin["Électronique"]["Casque"] = {"prix": 150, "quantite": 75}
print("Catégorie 'Électronique' mise à jour après l'ajout du Casque :")
print(inventaire_magasin["Électronique"])
print("-" * 30)

# Modifiez la quantité de "T-shirt" à 180.
inventaire_magasin["Vêtements"]["T-shirt"]["quantite"] = 180
print("Dictionnaire inventaire_magasin complet après modification du T-shirt :")
print(inventaire_magasin)
print("-" * 30)

# Calculez et affichez la valeur totale de tous les "Téléphone" en stock
prix_telephone = inventaire_magasin["Électronique"]["Téléphone"]["prix"]
quantite_telephone = inventaire_magasin["Électronique"]["Téléphone"]["quantite"]
valeur_totale_telephone = prix_telephone * quantite_telephone
print(f"La valeur totale des 'Téléphone' en stock est : {valeur_totale_telephone}€")
print("-" * 30)

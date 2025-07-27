'''code 1'''
class Chien:
    # Le constructeur : c'est une méthode spéciale qui est appelée quand on crée un nouvel objet
    def __init__(self, nom, race):
        self.nom = nom  # Attribut 'nom'
        self.race = race  # Attribut 'race'

    # Une méthode : le chien peut aboyer
    def aboyer(self):
        return f"{self.nom} dit Wouaf !"

# Création de deux objets de la classe Chien
mon_chien = Chien("Buddy", "Golden Retriever")
ton_chien = Chien("Rex", "Berger Allemand")

# Accéder aux attributs des objets
print(f"Mon chien s'appelle {mon_chien.nom} et est un {mon_chien.race}.")
print(f"Ton chien s'appelle {ton_chien.nom} et est un {ton_chien.race}.")

# Appeler les méthodes des objets
print(mon_chien.aboyer())
print(ton_chien.aboyer())



'''code 2'''
class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def afficher_details(self):
        return f"Titre : {self.titre}, Auteur : {self.auteur}, Année : {self.annee_publication}"

# Création d'objets Livre
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", 1954)
livre2 = Livre("1984", "George Orwell", 1949)

# Afficher les détails des livres
print(livre1.afficher_details())
print(livre2.afficher_details())



'''code 3'''
class voiture:
  def __init__ (self, marque, modele, annee):
    self.marque = marque
    self.modele = modele
    self.annee = annee

  def afficher_details(self):
    return f"Marque : {self.marque}, Modèle : {self.modele}, Année : {self.annee} \n Bip bip bip bip"

voiture1 = voiture("Toyota", "Camry", 2022)
voiture2 = voiture("Ford", "Mustang", 2021)

print(voiture1.afficher_details())
print(voiture2.afficher_details())


'''code 4'''
class Car:
   # Class attribute (shared by all instances)
   max_speed = 120  # Maximum speed in km/h


   # Constructor method (initialize instance attributes)
   def __init__(self, make, model, color, speed=0):
       self.make = make
       self.model = model
       self.color = color
       self.speed = speed  # Initial speed is set to 0


   # Method for accelerating the car
   def accelerate(self, acceleration):
       if self.speed + acceleration <= Car.max_speed:
           self.speed += acceleration
       else:
           self.speed = Car.max_speed


   # Method to get the current speed of the car
   def get_speed(self):
       return self.speed

# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)

# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")


'''code 5'''
#création de la classe chat
class chat:

  #methode constructeur
  def __init__ (self, nom, race):
    self.nom = nom #nom du chat
    self.race = race  #race du chat

  #création d'instances
  chat1 = chat("Miaou", "Siamois")
  chat2 = chat("Ronron", "Persan")

  # 3. Accès aux attributs :
  print(f"Le chat s'appelle {chat1.nom} et est de race {chat1.race}.")
  print(f"Le chat s'appelle {chat2.nom} et est de race {chat2.race}.")

  # 4. Modification d'un attribut :
  chat2.race = "Main Coon"
  print(f"{chat2.nom} est maintenant de race {chat2.race}.")



  '''code 6'''
  #création de class

class produit:

    #méthode contructeur
    def __init__(self, nom, prix, quantite):
      self.nom = nom
      self.prix = prix
      self.quantite = quantite

    #méthode d'instance d'affichage
    def afficher_details(self):
      return f" Nom: {self.nom}, Prix: {self.prix}€, quantité en stock:{self.quantite}"

    #methode d'instance vendre
    def vendre(self, nbr_vendus):

      if self.quantite - nbr_vendus < 0 :
        print (f"Quantité insuffisante en stock.")
      else:
        self.quantite -= nbr_vendus
        print (f"félicitation pour avoir vendu {nbr_vendus} {self.nom}, nous avons désormais {self.quantite} {self.nom} dans le stock")

#création d'object
ordinateur = produit("ordinateur portable", 950, 10)

print(ordinateur.afficher_details())

#vendre
ordinateur.vendre(2)
ordinateur.vendre(10)

print(ordinateur.afficher_details())


'''code 7'''
class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def afficher_details(self):
        print(f"Nom: {self.nom}, Prix: {self.prix}€, Quantité en stock: {self.quantite}")

    def vendre(self, nbr_vendus):
        if nbr_vendus <= 0:
            print("Le nombre d'articles vendus doit être positif.")
            return 

        if nbr_vendus <= self.quantite:
            self.quantite -= nbr_vendus
            print(f"{nbr_vendus} unités de {self.nom} vendues. Nouvelle quantité en stock : {self.quantite}.")
        else:
            print(f"Quantité insuffisante en stock pour {self.nom}. Seulement {self.quantite} disponibles.")

# Instanciation et interaction :
ordinateur = Produit("Ordinateur Portable", 950, 10)

print("--- État initial ---")
ordinateur.afficher_details()

print("\n--- Première vente (2 unités) ---")
ordinateur.vendre(2)

print("\n--- Deuxième vente (10 unités) ---")
ordinateur.vendre(10) 

print("\n--- Vente avec quantité négative (test erreur) ---")
ordinateur.vendre(-1)

print("\n--- État final ---")
ordinateur.afficher_details()



'''code 8'''
#création de la première class dédiée aux livres

class livre :
  #initialisation du nombre de livre
  nombre_total_livres = 0

  #méthode constructeur
  def __init__(self, "titre", "auteur", "annee_publication"):
    self.titre = titre
    self.auteur = auteur
    self.annee_publication = annee_publication
    livre.nombre_total_livres += 1

  def get_infos(self):
    print(f"titre du livre: {self.titre}, l'auteur: {self.auteur}, l'année de publication: {self.annee_publication}")


#partie 2: création de la première class dédiée à la bibliothèque
class Bibliotheque :
    def __init__(self):
      self.collection = [] #liste pour stocker les object livre

    def ajouter_livre(self, livre):



'''code 9'''
# Partie 1 : La classe Livre
class Livre:
    # Attribut de classe : partagé par toutes les instances de Livre
    nombre_total_livres = 0

    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        Livre.nombre_total_livres += 1 # Incrémente l'attribut de classe à chaque nouvelle instance

    def get_infos(self):
        return f"Titre: '{self.titre}', Auteur: {self.auteur}, Année: {self.annee_publication}"

# Partie 2 : La classe Bibliotheque
class Bibliotheque:
    def __init__(self):
        self.collection = [] # Une liste pour stocker les objets Livre

    def ajouter_livre(self, livre):
        if isinstance(livre, Livre): # S'assurer que l'objet est bien une instance de Livre
            self.collection.append(livre)
            print(f"'{livre.titre}' a été ajouté à la bibliothèque.")
        else:
            print("Erreur : Seuls des objets Livre peuvent être ajoutés à la collection.")

    def lister_livres(self):
        if not self.collection:
            print("La bibliothèque est vide.")
            return

        print("\n--- Livres dans la bibliothèque ---")
        for livre in self.collection:
            print(livre.get_infos())
        print("---------------------------------")

    def chercher_par_auteur(self, nom_auteur):
        trouves = []
        for livre in self.collection:
            if livre.auteur == nom_auteur:
                trouves.append(livre)

        if trouves:
            print(f"\n--- Livres de {nom_auteur} ---")
            for livre in trouves:
                print(livre.get_infos())
            print("---------------------------------")
        else:
            print(f"\nAucun livre trouvé pour l'auteur '{nom_auteur}'.")

# Partie 3 : Utilisation des classes et objets :

# Créer une instance de Bibliotheque
ma_bibliotheque = Bibliotheque()

# Créer des objets Livre
livre1 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
livre2 = Livre("1984", "George Orwell", 1949)
livre3 = Livre("La Ferme des Animaux", "George Orwell", 1945)
livre4 = Livre("Vingt Mille Lieues sous les mers", "Jules Verne", 1870)

# Ajouter ces livres à ma_bibliotheque
ma_bibliotheque.ajouter_livre(livre1)
ma_bibliotheque.ajouter_livre(livre2)
ma_bibliotheque.ajouter_livre(livre3)
ma_bibliotheque.ajouter_livre(livre4)

# Appeler ma_bibliotheque.lister_livres()
ma_bibliotheque.lister_livres()

# Afficher le nombre_total_livres de la classe Livre
print(f"\nNombre total de livres créés (attribut de classe) : {Livre.nombre_total_livres}")

# Appeler ma_bibliotheque.chercher_par_auteur("George Orwell")
ma_bibliotheque.chercher_par_auteur("George Orwell")

# Appeler ma_bibliotheque.chercher_par_auteur("Jules Verne")
ma_bibliotheque.chercher_par_auteur("Jules Verne")

# Test d'un auteur inconnu
ma_bibliotheque.chercher_par_auteur("Victor Hugo")


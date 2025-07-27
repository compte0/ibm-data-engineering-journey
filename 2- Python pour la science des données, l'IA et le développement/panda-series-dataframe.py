'''code 1'''
# Création d'une Series simple
s = pd.Series([10, 20, 30, 40, 50])
print(f"Series à partir d'une liste :\n", s)


'''code 2'''
# Series avec un index personnalisé
s_fruits = pd.Series([25, 12, 8], index=['Pommes', 'Bananes', 'Oranges'])
print("\nSeries avec index personnalisé :\n", s_fruits)



'''code 3'''
# Series à partir d'un dictionnaire
data_dict = {'Maths': 90, 'Physique': 85, 'Chimie': 78}
s_notes = pd.Series(data_dict)
print("\nSeries à partir d'un dictionnaire :\n", s_notes)



'''code 4'''
# Création d'un DataFrame à partir d'un dictionnaire de listes
data_ventes = {
    'Produit': ['Ordinateur', 'Souris', 'Clavier', 'Écran'],
    'Quantite': [10, 50, 30, 5],
    'Prix_Unitaire': [1200.00, 25.00, 75.00, 300.00],
    'En_Stock': [True, True, False, True]
}
df_produits = pd.DataFrame(data_ventes)
print(f"DataFrame de produits :\n", df_produits)


'''code 5'''
import pandas as pd
# Création d'un DataFrame à partir d'une liste de dictionnaires
data_clients = [
    {'ID': 1, 'Nom': 'Alice', 'Ville': 'Paris'},
    {'ID': 2, 'Nom': 'Bob', 'Ville': 'Lyon'},
    {'ID': 3, 'Nom': 'Charlie', 'Ville': 'Marseille'}
]
df_clients = pd.DataFrame(data_clients)
print(f"\nDataFrame de clients :\n", df_clients)


'''code 6'''
# Création d'un DataFrame à partir d'une liste de dictionnaires
data_clients = [
    {'ID': 1, 'Nom': 'Alice', 'Ville': 'Paris'},
    {'ID': 2, 'Nom': 'Bob', 'Ville': 'Lyon'},
    {'ID': 3, 'Nom': 'Charlie', 'Ville': 'Marseille'},
    {'ID': 4, 'Nom': 'peter', 'Ville': 'Nice'},
    {'ID': 5, 'Nom': 'alice', 'Ville': 'Montpellier'},
    {'ID': 6, 'Nom': 'jane', 'Ville': 'Nantes'},
    {'ID': 7, 'Nom': 'tom', 'Ville': 'Metz'}
]
df_clients = pd.DataFrame(data_clients)
print("\nDataFrame de clients :\n", df_clients)

print("\nIndex de df_produits :", df_clients.index)
print("Colonnes de df_produits :", df_clients.columns)
print("Dimensions de df_produits :", df_clients.shape)
print("Types de données de df_produits :\n", df_clients.dtypes)

print("\nPremières lignes de df_produits :\n", df_clients.head(2))
print("\nInfos sur df_produits :\n", df_clients.info())
print("\nStatistiques descriptives de df_produits :\n", df_clients.describe())
'''programme demande le nom et l'age de l'utilisateur
et renvoyant ses efformation sous forme de phrase tout en te rassurant
que se dernier n'a pas entrer des information erronées'''

def information_des_users(nom, age):
  print(f"Ravi de vous rencontrer {nom}, vous avez {age} ans")
  print(f"L'année prochaine, vous aurez {age + 1} ans")

def demande_nom():
    reponse_nom = ""
    while reponse_nom == "" or reponse_nom == " ":
      reponse_nom = input (f"Veuiller entrer votre nom : ")
    return reponse_nom

def demande_age():
  age_user=0
  while age_user == 0:
      age_str = input("Veuillez entrer votre âge: ")
      try:
        age_user = int(age_str)
      except:
        print("ERREUR: vous devez entrer un nombre pour l'âge.")
  return age_user

#demander nom
nom1 = demande_nom()
nom2 = demande_nom()

#demander age
age1 = demande_age()
age2 = demande_age()

#affichage des informations des utilisateur
information_des_users(nom1, age1)
information_des_users(nom2, age2)
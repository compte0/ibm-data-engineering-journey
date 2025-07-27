# Tuples d'entiers
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
tuple_combiner = tuple_a + tuple_b
print (f"nous obtenons le tuple: {tuple_combiner}")

# Tuples d'entiers
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple_combine1 = tuple1 + tuple2
print(f"Combinaison d'entiers : {tuple_combine1}") # (1, 2, 3, 4, 5, 6)

jours_semaine  = ("lundi", "mardi")
semaine_complete = jours_semaine * 3
print (f"la semaine complète est : {semaine_complete}")

alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
nombre_de_caractere = len(alphabet)
debut_alphabet = alphabet [0:3]
milieu_alphabet = alphabet [3:7]
fin_alphabet = alphabet [7:nombre_de_caractere]
print(f"les lettres du début sont : {debut_alphabet} \n ceux du milieu sont : {milieu_alphabet} \n et ceux de la fin sont : {fin_alphabet}")

tuple_pas = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
#pour chaque index pair
nombres_pairs_index = tuple_pas[::2]
print(f"Les valeurs de ce tuple ayant des index paire sont: {nombres_pairs_index}")
#pour chaque index impair
nombres_impairs_index = tuple_pas[1::2]
print(f"Les valeurs de ce tuple ayant des index impaire sont: {nombres_impairs_index}")
#pour le tuple inverse
tuple_inverse = tuple_pas[::-1]
print(f"Le tuple inverse du est :{tuple_inverse}")
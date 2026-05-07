import sys, random

#region List
# print("1. Liste - Modifiable, ordonnée, doublons autorisés")
# liste = list()
# liste = [10,20,30,40]

# # Ajouter un élément a la fin
# liste.append(50)

# # Modifier l'élément 30 par 99
# liste[2] = 99

# # Insérer l'élément 100 après 99 => [10,20,99,40]
# liste.insert(3,100)


# print("Liste =>", liste)
# liste.sort()
# print("Liste trié =>", liste)

# print("premier élément de la liste : ", liste[0])
# print("dernier élément de la liste : ", liste[-1])

#endregion

#region Tuple

# print("2. Tuple - Immuable (on ne plus changer les valeurs)")

# mon_tuple = tuple()
# mon_tuple = (100,200,300,400)
# mon_tuple2 = (100,200,300,400)

# mon_tuple3 = mon_tuple + mon_tuple2

# print("tuple 3 :", mon_tuple3)

# # Immuable donc impossible de changer la valeur
# # mon_tuple[1] = 999

# # Déballage 
# valeur_a, valeur_b, valeur_c, valeur_d = mon_tuple

# print("Déballage :", valeur_a, valeur_b, valeur_c, valeur_d, sep="\n- ")


#endregion

#region Set

# print("3. Set - Éléments unique, non ordonnée")

# mon_set = set()
# mon_set = {5,10,15,20}
# mon_set_2 = {5,10,99,20}

# print("Différence mon_set / mon_set_2", mon_set.difference(mon_set_2))
# print("Différence mon_set / mon_set_2", mon_set_2.difference(mon_set))

# # Ajouter un élément
# mon_set.add(25)

# # Supprimer un élément
# mon_set.discard(5)
# print(mon_set)

# # Vérifier la présence d'un élément
# print("15 est dedans ?", 15 in mon_set)

#endregion

#region Dictionnaire

# print("4. Dictionnaire - Clé => valeur")

# personne = {
# 	"prenom" : "Nicolas",
# 	"age" : 26,
# 	"ville" : "Bruxelles"
# }

# print("personne :", personne)

# personne['prenom'] = "Toto"

# max_int = sys.maxsize
# print("max int => ", type(max_int))

# personne['salaire_annuel'] = max_int

# print("élément supprimé de mon dictionnaire :", personne.pop("ville"))

# for cle, valeur in personne.items():
# 	print(f"-{cle} => {valeur}", sep="\n")

#endregion

ma_liste = []

for index in range(5):
	ma_liste.append(random.randint(1,100))

print(ma_liste)
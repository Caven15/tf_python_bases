note = int(input("Entrez une note : "))

# if (note < 0) or (note > 20):
# 	print("La note n'est pas comprise entre 0 et 20")
# else :
# 	if (note >= 16) :
# 		print("Très bien ✅")
# 	elif (note >= 12) :
# 		print("sSatisfaisant ✅")
# 	elif (note >= 10) :
# 		print("Passable ⚠️")
# 	else :
# 		print("Insuffisant (Pas de bonbons...) ❌")

# if (note < 0) or (note > 20):
# 	print(f"La note '{note}' n'est pas comprise entre 0 et 20")
# else :
# 	match note:
# 		case n if n >= 16 :
# 			print("Très bien ✅")
# 		case n if n >= 12 :
# 			print("bien ✅")
# 		case n if n >= 10 :
# 			print("Passable ⚠️")
# 		case _ :
# 			print("Insuffisant (Pas de bonbons...) ❌")

if (note < 0) or (note > 20):
	print(f"La note '{note}' n'est pas comprise entre 0 et 20")
else :
	match note:
		case 16 | 17 | 18 | 19 | 20 :
			print("Très bien ✅")
		case 12 | 13 | 14 | 15 :
			print("bien ✅")
		case 10 | 11 :
			print("Passable ⚠️")
		case _ :
			print("Insuffisant (Pas de bonbons...) ❌")
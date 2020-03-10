from mulTwolnt import mul

a="x"
while((a!="y") or (a!="q")):
	a=input("Pour multiplier appuyez sur la touch y, pour quitter appuyez q" + " ")
	if (a=="y"):
		try:
			a=int(input("Entrez la valeur 1: "))
			b=int(input("Entrez la valeur 2: "))
			print("Le resultas est: " + str(mul(a,b)))
		except Exception as e:
			print("Entrez invalide")
	elif (a=="q"):
		break
	else:
		print("Entrez invalide")

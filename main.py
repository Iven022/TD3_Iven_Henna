<<<<<<< HEAD

from addTwoInt import add

x="y"
while((x=="y") or (x=="q")):
	x=input("For Addition of two numbers press < y > or to quit press < q >" + "  ")
	if (x=="y"):
		try:
			a=int(input("Enter first number"))
			b=int(input("Enter Second number"))
			print("Your result is: " + str(add(a,b)))
		except Exception as e:
			print("Invalid Input, try again")
	elif (x=="q"):
		break
	else:
		print("Invalid input, try again")
		x="y"





=======
from mulTwolnt import mul

a="y"
while((a=="y") or (a=="q")):
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
		a="y"
>>>>>>> a21b9efca9f907198f26f5c28e6bf8175463ab57

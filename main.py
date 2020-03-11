
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






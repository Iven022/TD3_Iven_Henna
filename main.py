
from addTwoInt import add
from mulTwolnt import mul

x="a"
while((x=="a") or (x=="q") or (x=="b")):
	print("For Addition of two numbers press < a > ")
	print("For multiplacation press < m > ")
	print("For both calculations press < b > ")
	print("To quit press < q > ")
	x=input("Enter desired process ")
	if ((x=="a") or (x=="m") or (x=="b")):
		try:
			a=int(input("Enter first number   "))
			b=int(input("Enter Second number   "))
			if (x=="a"):
				print("Your Addition  result is: " + str(add(a,b)))
			elif (x=="m"):
				print("Your Multiplication result is " + str(mul(a,b)))
				x=="m"
			else:
				print("Your Addition  result is: " + str(add(a,b)))
				print("Your Multiplication result is " + str(mul(a,b)))
				x=="a"
			print("  ")
			print("  ")
			z=input("More Calculations ? Press < y > for more or < n > to stop ")
			if (z=="y"):
				x=="a"
			elif(z=="n"):
				break
			else:
				print("Invalid input")
				break

		except Exception as e:
			print("Invalid Input, try again")
	elif (x=="q"):
		break
	else:
		print("Invalid input, try again")
		x="a"



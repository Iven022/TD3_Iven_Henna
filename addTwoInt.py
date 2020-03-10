import sys
def add(x,y):
  	return int(x)+int(y)

if __name__=="__main__":
	try:
		if (len(sys.argv)>3):
			print("Too many values Entered")
		else:
			print(add(sys.argv[1],sys.argv[2]))
	except Exception as e:
		print("Not Enough Values Entered")
		x=len(sys.argv)
		CopyArg=sys.argv
		while(x<3):
			CopyArg.append(int(input("Enter value number " + str(x) + "    ")))
			x+=x
		print(add(CopyArg[1],CopyArg[2]))



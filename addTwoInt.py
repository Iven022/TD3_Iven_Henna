import sys
def add(x,y):
	return int(x)+int(y)

if __name__=="__main__":
	if (len(sys.argv)==3):
		print(add(sys.argv[1],sys.argv[2]))
	elif (len(sys.argv)>3):
		print("Too much values entered")
	else:
		print("Not enough values entered")



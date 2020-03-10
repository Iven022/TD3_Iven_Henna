import sys
def mul(a,b):
	return int(a)*int(b)

if __name__ == "__main__":
	try:
		if (len(sys.argv)>3):
			print("Inserez que deux valeur")
		else:
			print(mul(sys.argv[1],sys.argv[2]))
	except Exception as e:
		print("Inserez 2 valeur")
		i=len(sys.argv)
		CopyArg=sys.argv
		while(i<3):
			CopyArg.append(int(input("Valeurs " + str(i) + ": ")))
			i+=i
		print(mul(CopyArg[1],CopyArg[2]))


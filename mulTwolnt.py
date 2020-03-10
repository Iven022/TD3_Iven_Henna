import sys
def mul(a,b):
	return int(a)*int(b)

if __name__ == "__main__":
	print(sys.argv)
	print(mul(sys.argv[1],sys.argv[2]))

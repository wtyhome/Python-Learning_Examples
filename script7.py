while (1):
	inpStr=input("Please enter integers(to split,use \",\")")
	inp=inpStr.split(",")
	print("Origin list: " + str(inp))
	copyInp=inp[:]
	inp[0]=-1
	print("Origin list: " + str(inp))
	print("Copied list: " + str(copyInp))

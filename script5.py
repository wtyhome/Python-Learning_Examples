while (1):
	minNumber=0
	inpStr=input("Please input more then 1 integers(to split,use \",\"): ")
	inp=[]
	for ele in inpStr.split(","):
		inp.append(int(ele))

	minNumber=min(inp)
	inp.sort()
	print(inp)
	print("Minimun number is %d" % int(minNumber))


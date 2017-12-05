#main
while(1):
	inp=input("Please enter strings splited by \",\"").split(",")
	for strs in inp:
		print(strs + " ",end="")
	print("")
#main
while(1):
	inp=input("Please input strings splited by \" \": ").split(" ")
	for splited_str in inp[::-1]:
		print(splited_str + " ",end="")
	print("")

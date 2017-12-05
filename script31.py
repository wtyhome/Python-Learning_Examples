import vb
#main
inp=""
while (1):
	inp = input("Please input a char:")
	if (inp=="M" or inp=="m"):
		print("Monday")#1
		continue
	elif(inp=="W" or inp=="w"):
		print("Wednesday")#3
		continue
	elif(inp=="F" or inp=="f"):
		print("Friday")#5
		continue
	elif (inp=="T"or inp =="t"):
		inp=input("Please input second char:")
		if (inp=="U" or inp == "u"):#2
			print("Tuesday")
			continue
		elif(inp=="H" or inp == "h"):#4
			print("Thursday")
			continue
	elif(inp=="S" or inp=="s"):
		inp=input("Please input second char:")
		if (inp=="A" or inp =="a"):#6
			print("Saturday")
			continue
		elif(inp=="U" or inp=="u"):#7
			print("Sunday")
			continue
	print("Char(s) you inputted doesn't exist in our set")

#main
while(1):
	inp=input("Please enter a line of string: ")
	print("")
	letters=0
	spaces=0
	digits=0
	others=0
	for ch in inp:
		if (ch.isalpha()):
			letters+=1
		elif(ch.isspace()):
			spaces+=1
		elif(ch.isdigit()):
			digits+=1
		else:
			others+=1
	print("Letter count: %d" % letters)
	print("Spaces count: %d" % spaces)
	print("Digits count: %d" % digits)
	print("Others count: %d" % others)
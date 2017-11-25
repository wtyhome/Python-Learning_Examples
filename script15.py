#main
while (1):
	inp=input("Please enter your score(0~100)")
	score=int(inp)
	if (score > 100 or score <0):
		print("This is not a valid score")
		continue
	
	if (score >=90):
		print("A")
	elif(score >=60):
		print("B")
	else:
		print("C")

#digits cube sum equal to itself
while (1):
	inp=input("Please input an integer: ")
	sum=0
	for ch in inp:
		print(int(ch)**3)
		sum+=int(ch)**3

	if (sum ==int(inp)):
		print("Yes")
	else:
		print("No")



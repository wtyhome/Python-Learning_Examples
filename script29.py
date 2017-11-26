#main
while (1):
	inp = input("Please enter an integer: ")
	digitCount=len(inp)
	revInp=inp[::-1]
	print("%d digits, %s(reversed)" % (digitCount,revInp))

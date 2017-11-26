#functions
def IsLoopStr(inp):
	revInp=inp[::-1]
	if (inp == revInp):
		return True
	else:
		return False
#main
while(1):
	inp=input("Please enter an integer: ")
	if (IsLoopStr(inp)):
		print("This is a Palindrome")
	else:
		print("This is not a Palindrome")
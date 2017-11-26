#functions
def f(inp):
	temp=""
	if (len(inp)<=1):
		temp=inp
		return temp
	else:
		temp=inp[len(inp)-1]+f(inp[:len(inp)-1])
		return temp
#main
while(1):
	inp=input("Please enter a string")
	print(f(inp))
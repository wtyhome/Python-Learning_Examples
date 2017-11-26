#day 1 x -> x/2-1
#day 2 x/2-1=y -> y/2-1
#day 3 y/2-1=z -> z/2-1
#...
#day 10 1 -> stop

#functions
def f(inpN):
	n=int(inpN)
	if (n==1):
		return 1
	else:
		return (f(n-1)+1)*2

#main
while (1):
	inp=input("Please enter an integer: ")
	print(f(int(inp)))
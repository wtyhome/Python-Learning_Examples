#functions
def f(inpN):
	n=int(inpN)
	if (n==1):
		return 10
	else:
		return f(n-1)+2
#main
print(f(5))
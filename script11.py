#globals
dp=[-1]*100000
#functions
def f(inp):
	n=int(inp)
	if (dp[n]==-1):
		if (n<=2):
			dp[n]=1
		else:
			dp[n]=f(n-1)+f(n-2)
	return dp[n]

#main
while (1):
	inp = int(input("Please enter an integer: "))
	if (inp <=0 or inp >=1000):
		print("This integer is not valid(<=0 or >=1000)")
		continue
	print(f(inp))

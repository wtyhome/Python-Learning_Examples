#functions
def f(n):
	if (n==0):
		print("%d! = %d"%(0,1))
		return 1
	else:
		temp=f(n-1)*n
		print("%d! = %d" %(n,temp))
		return temp

#main
f(5)
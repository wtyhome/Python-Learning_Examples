import math
#functions
def IsPrime(InpN):
	n=int(InpN)
	if (n == 1 or n == 0):
		return False
	LastCheckNumber=int(math.sqrt(n))
	for i in range(2,LastCheckNumber+1):
		if (n % i==0):
			return False
	return True
#main
for number in range(1,101):
	if (IsPrime(number)):
		print(number)

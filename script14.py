#functions
def Factorization(inp):
	num=int(inp)
	if (num == 0):
		return 0

	if(num == 1):
		return 1

	ret=""
	i = 2
	while (num != 1):
		while (num % i != 0):
			i+=1

		while (num % i == 0):
			num /=i
			ret +=str(i)+"*"

	ret = ret[:len(ret)-1]
	return ret
#main
while (1):
	inp=input("Please enter an integer: ")
	print(Factorization(inp))
import random
#functions
def createRandomList():
	n=11
	ret=[]
	for i in range(0,n):
		ret.append(random.randint(-100,100))
	print(ret)
	return ret
def reverseList(L):
	n=11
	for i in range(0,int(n/2)):
		temp=L[i]
		L[i]=L[n-1-i]
		L[n-1-i]=temp
	print("After:\n "+str(L))
#main
L=createRandomList()
reverseList(L)
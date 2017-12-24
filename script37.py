import random
#functions
def GetTenRandomInt():
	ret=[]
	for i in range(1,11):
		ret.append(random.randint(-10000,10000))
	print("Created 10 random numbers,they are " + str(ret))
	return ret

def GetListCount(Inp):
	ret=0
	print(Inp)
	for ele in Inp:
		ret+=1
	return ret

def bubblesort(Inp):
	ListCount=GetListCount(Inp)
	for i in range(0,ListCount):
		for j in range(0,ListCount-1):
			if (Inp[j] > Inp[j+1]):
				temp=Inp[j]
				Inp[j]=Inp[j+1]
				Inp[j+1]=temp

#main
randomInts=GetTenRandomInt()
bubblesort(randomInts)
print(randomInts)
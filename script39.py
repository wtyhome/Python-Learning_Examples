import random
#functions
def GetRandonInts(InpN):
	n=int(InpN)
	ret=[]
	for i in range(0,InpN):
		ret.append(random.randint(-100,100))
	return ret

def UserInput():
	UserListSize=-1
	UserInsertPosition=-1
	while (UserListSize==-1):
		UserListSize=int(input("Please input list size: "))
		if (UserListSize < 0):
			UserListSize=-1
	while (UserInsertPosition==-1):
		UserInsertPosition=int(input("Please input the position you wanted to insert(base 0): "))
		if (UserInsertPosition < 0 or UserInsertPosition > UserListSize):
			UserInsertPosition=-1
	return (GetRandonInts(UserListSize),UserListSize,UserInsertPosition,)

def InsertToList(InpList,InpUserListSize,InpInsertPos):
	L=InpList
	InsertPos=int(InpInsertPos)
	UserListSize=int(InpUserListSize)
	print("Before:\n"+ str(L))
	L.append(0)
	for i in range(InpUserListSize-1,InpInsertPos-1,-1):
		L[i+1]=L[i]
	L[InsertPos]=int(input("Number you wanted to insert: "))
	print("After:\n"+str(L))
#main
L,UserListSize,UserInsertPosition=UserInput()
InsertToList(L,UserListSize,UserInsertPosition)

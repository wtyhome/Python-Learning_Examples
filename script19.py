#functions
def FindFactors(inpNum):
	num=int(inpNum)
	ret=[]
	if (num==0 or num==1):
		return [num]
	for i in range(1,inpNum):
		if (inpNum % i ==0):
			ret.append(i)
	return ret

def IsPerfectNumber(inpNum,inpList):
	num=int(inpNum)
	sum=0
	for ele in inpList:
		sum+=ele
	if (sum == num):
		return True
	else:
		return False
#main
for num in range(2,1001):
	factor=FindFactors(num)
	if (IsPerfectNumber(num,factor)):
			print(num)
			print(factor)


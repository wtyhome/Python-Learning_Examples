#<=100000 part+10%
#>100000 <=200000 part+7.5%
#>200000 <=400000 part+5%
#>400000 <=600000 part+3%
#>600000 <=1000000 part+1.5%
#>1000000 part+1%

totalAmount=0
tempAmount=0
stageAmount=[0,100000,200000,400000,600000,1000000]
stageRate=[0.1,0.075,0.05,0.03,0.015,0.01]
while (1):
	originEarn=int(input("Please enter net income: "))
	for i in range(0,6):
		tempAmount=originEarn
		if (i==0):
			if (tempAmount>100000):
				tempAmount=100000
		elif(i==5):
			tempAmount-=stageAmount[i]
			if (tempAmount<=0):
				break
		else:
			tempAmount-=stageAmount[i-1]
			tempAmount-=stageAmount[i]
			if (tempAmount<=0):
				break
		totalAmount+=tempAmount*stageRate[i]
		print(totalAmount)

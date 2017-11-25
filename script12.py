import math
#math.ceil↑
#math.floor↓
#round 5↑4↓
#math.sqrt(n) n^0.5
count=0
for num in range(101,201):
	Flag=True
	for i in range(2,math.floor(math.sqrt(num))+1):
		if (num % i ==0):
			Flag=False
	if (Flag==True):
		print(num)
		count+=1
print("The total is %d"%count)

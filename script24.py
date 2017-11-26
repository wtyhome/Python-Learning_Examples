#functions
def f1(inpN):
	#2 3 5 8 13 21
	n=int(inpN)
	if (n==1 or n==2):
		return n+1
	else:
		return f1(n-1)+f1(n-2)
def f2(inpN):
	#1 2 3 5 8 13
	n=int(inpN)
	if (n==1 or n==2):
		return n
	else:
		return f2(n-1)+f2(n-2)
#main
s=0.0
temp=0.0
for i in range(1,21):
	temp=(f1(i)/f2(i))
	print(temp)
	s+=temp
print("Total :" + str(s))
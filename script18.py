#main
while(1):
	n=input("Please enter an base digit ")
	r=input("Please enter number of repeatition time ")
	if (not n.isnumeric()):
		print("base digit is not valid")
		continue
	if (not r.isnumeric()):
		print("repeatition time is not valid")
		continue
	sum=0
	temp=""
	for i in range(1,int(r)+1):
		temp=int(n*i)
		print(temp)
		sum+=int(temp)

	print("Result: " + str(sum))
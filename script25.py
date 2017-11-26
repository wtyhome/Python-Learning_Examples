#main
s=0
temp=1
for i in range(1,21):
	temp*=i
	print(temp)
	s+=temp
print("Total :" + str(s))
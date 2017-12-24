import random
#function
def createdMatrix(width,height):
	m=[]
	#created double array random int element 
	for i in range(0,height):
		m.append([])
		for j in range(0,width):
			m[i].append([])
			m[i][j]=random.randint(1,100)
	return m
def showMatrix(m):
	for row in m:
		for ele in row:
			print(str(ele) + " ",end="")
		print("")
def mainDiagonalSum(m):
	sum=0
	i=-1
	j=-1
	for row in m:
		i+=1
		for ele in row:
			j+=1
			if (i == j): 
				sum+=int(ele)
		j=-1
	print("Sum=" + str(sum))
#main
m=createdMatrix(3,3)
showMatrix(m)
mainDiagonalSum(m)

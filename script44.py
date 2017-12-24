import random
#functions
def GetRandomMatrix(height_,width_):
	height=int(height_)
	width=int(width_)
	ret=[]
	for i in range(0,height):
		ret.append([])
		for j in range(0,width):
			ret[i].append(random.randint(-100,100))
	showMatrix(ret)
	return ret
def addMatrix(m1,m2):
	m=[]
	h=len(m1)
	w=len(m1[0])
	for i in range(0,h):
		m.append([])
		for j in range(0,len(m1[0])):
			m[i].append(m1[i][j]+m2[i][j])
	showMatrix(m)
	return m
def showMatrix(m):
	for row in m:
		for ele in row:
			print(str(ele)+" ",end="")
		print("")
	print("")
#main
m1=GetRandomMatrix(3,3)
m2=GetRandomMatrix(3,3)
m=addMatrix(m1,m2)
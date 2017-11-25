import calendar
def IsGapYear(y):
	if ((y % 4 == 0 and y % 100 !=0)or y %400==0):
		return True
	else:
		return False

def CalculateDays(y,m,d):
	i=1
	sum=0
	while (i<m):
		sum+=calendar.mdays[i]
		i+=1
	i=1
	while (i<=d):
		sum+=1
		i+=1
	return sum

y=0
m=0
d=0
i=0
ans=0
inp=""
lis=[]
while (1):
	inp=input("Please enter date information(yy/mm/dd)").split("/")
	y=int(inp[0])
	m=int(inp[1])
	d=int(inp[2])
	if (m>12 or m < 0):
		print("Input date error: no such month(>12 or <0)")
		continue
	if (d < 1 or d>calendar.mdays[m]):
		print("Input date error: no such day in this year")
		continue
	ans=CalculateDays(y,m,d)
	if (m > 2 and IsGapYear(y)):
		ans+=1
	print("Today is the %sth day in this year" % ans)

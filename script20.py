#main
n=10
height=100.0
total=0.0
for i in range(1,n+1):
	print("Round %d"%i)
	#goes down
	total+=height
	print("Goes down %f meter(s)" % height)
	#height / 2
	height/=2
	#goes up
	if (i < n):
		total+=height
		print("Goes up %f meter(s)" % height)
print("Total %f meter(s)" % total)

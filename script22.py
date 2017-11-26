#main
players=['x','y','z']
for a in range(0,3):#a's opponent
	for b in range(0,3):#b's opponent
		for c in range(0,3):#c's opponent
			if (a==b or b==c or a==c):
				continue
			if (players[a]=='x'):
				continue
			if (players[c]=='x'):
				continue
			if (players[c]=='z'):
				continue
			print("a:%s\nb:%s\nc:%s\n" % (players[a],players[b],players[c]))

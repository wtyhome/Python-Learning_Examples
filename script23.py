#1357531
import math
lines=1
stars=1
while (stars>0):
	print(" "*abs(4-lines)+"*"*stars)
	if (lines<4):
		stars+=2
	else:
		stars-=2
	lines+=1
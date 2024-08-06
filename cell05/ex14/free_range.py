#!/usr/bin/env python3
import sys
try :
	if len(sys.argv) != 3 :
		print("none")
	else :
		nbr0 = int(sys.argv[1].strip())
		nbr1 = int(sys.argv[2].strip())
		x = []
		if nbr0 < nbr1 :
			for i in range(nbr0, nbr1 + 1) :
				x.append(i)
		else :
			for i in range(nbr1, nbr0 + 1) :
				x.append(i)
		print(x)
except:
	print("An exception occurred.")
#!/usr/bin/env python3
try :
	nbr = float(input().strip())
	if nbr == 0 :
		print("This number is equal to zero.")
	else :
		print("This number is different from zero.")
except:
	print("An exception occurred.")
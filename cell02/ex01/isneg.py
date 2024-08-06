#!/usr/bin/env python3
try :
	nbr = float(input().strip())
	if nbr < 0 :
		print("This number is negative.")
	elif nbr > 0:
		print("This number is positive.")
	else :
		print("This number is both positive and negative.")
except:
	print("An exception occurred.")
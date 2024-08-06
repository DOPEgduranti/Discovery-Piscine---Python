#!/usr/bin/env python3
try :
	nbr0 = float(input("Give me the a number: ").strip())
	nbr1 = int(nbr0)
	nbr2 = float(nbr1)
	if nbr0 != nbr2 :
		print("This number is a decimal.")
	else :
		print("This number is an integer.")
except:
	print("An exception occurred.")
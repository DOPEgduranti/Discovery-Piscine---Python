#!/usr/bin/env python3
try :
	nbr0 = float(input("Enter the first number:\n").strip())
	nbr1 = float(input("Enter the second number:\n").strip())
	res = nbr0 * nbr1
	print(nbr0, " x ", nbr1, " = ", res)
	if res < 0 :
		print("The result is negative.")
	elif res > 0:
		print("The result is positive.")
	else :
		print("The result is positive and negative.")
except:
	print("An exception occurred.")
#!/usr/bin/env python3
try:
	nbr = int(input("Enter a number\n").strip())
	for x in range(10):
		print(x, " x ", nbr, " = ", x * nbr)
except:
	print("An exception occurred.")
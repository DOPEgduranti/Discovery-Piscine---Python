#!/usr/bin/env python3
try:
	nbr = int(input("Enter a number less than 25\n").strip())
	if nbr > 25 :
		print("Error")
	else :
		while nbr <= 25 :
			print("Inside the loop, my variable is ", nbr)
			nbr += 1
except:
	print("An exception occurred.")
#!/usr/bin/env python3
try :
	nbr0 = float(input("Give me the first number: ").strip())
	nbr1 = float(input("Give me the second number: ").strip())
	print("Thank you!")
	print(nbr0, "+", nbr1, "=", nbr0 + nbr1)
	print(nbr0, "-", nbr1, "=", nbr0 - nbr1)
	print(nbr0, "*", nbr1, "=", nbr0 * nbr1)
	if nbr1 != 0 :
		print(nbr0, "/", nbr1, "=", nbr0 / nbr1)
	else :
		print(nbr0, "/", nbr1, "= Impossible")
except:
	print("An exception occurred.")
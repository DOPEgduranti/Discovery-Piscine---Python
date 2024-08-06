#!/usr/bin/env python3
import math
try :
	nbr = float(input("Give me the a number: ").strip())
	print(math.ceil(nbr))
except:
	print("An exception occurred.")
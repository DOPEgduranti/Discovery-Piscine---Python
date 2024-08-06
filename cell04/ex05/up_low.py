#!/usr/bin/env python3
try :
	str = input()
	for i in str :
		if i >= 'A' and i <= 'Z' :
			print(i.lower(), end="")
		elif i >= 'a' and i <= 'z' :
			print(i.upper(), end="")
		else :
			print(i, end="")
	print()
except:
	print("An exception occurred.")
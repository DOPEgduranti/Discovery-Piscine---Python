#!/usr/bin/env python3
import sys
try:
	if len(sys.argv) != 1 :
		print("none")
	else :
		x = 0
		while x < 11 :
			print("Table de ", x, ":", end = "")
			y = 0
			while y < 11 :
				print(" ", x * y, end = "")
				y += 1
			print()
			x += 1
except:
	print("An exception occurred.")
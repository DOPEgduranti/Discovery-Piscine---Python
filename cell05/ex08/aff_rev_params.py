#!/usr/bin/env python3
import sys
try :
	if len(sys.argv) < 3 :
		print("none")
	else :
		i = len(sys.argv)
		while i > 1 :
			print(sys.argv[i - 1])
			i -= 1
except:
	print("An exception occurred.")
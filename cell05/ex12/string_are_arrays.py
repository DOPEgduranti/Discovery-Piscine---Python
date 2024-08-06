#!/usr/bin/env python3
import sys
import re
try :
	if len(sys.argv) != 2 :
		print("none")
	else :
		x = re.findall("z", sys.argv[1])
		if len(x) == 0 :
			print("none")
		else :
			for i in x :
				print("z", end="")
			print()
except:
	print("An exception occurred.")
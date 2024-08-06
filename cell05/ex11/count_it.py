#!/usr/bin/env python3
import sys
try :
	if len(sys.argv) < 2 :
		print("none")
	else :
		print("parameters:", len(sys.argv) - 1)
		for i in sys.argv[1:] :
			print(i + ":", len(i))
except:
	print("An exception occurred.")
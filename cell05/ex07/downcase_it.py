#!/usr/bin/env python3
import sys
try :
	if len(sys.argv) != 2 :
		print("none")
	else :
		print(sys.argv[1].lower())
except:
	print("An exception occurred.")
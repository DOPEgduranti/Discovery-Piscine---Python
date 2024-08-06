#!/usr/bin/env python3
import sys
import re
try :
	if len(sys.argv) != 3 :
		print("none")
	else :
		print(len(re.findall(sys.argv[1], sys.argv[2])))
except:
	print("An exception occurred.")
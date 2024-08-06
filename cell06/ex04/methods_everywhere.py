#!/usr/bin/env python3
import sys
def shrink(s:str) :
	x = slice(0, 8)
	print(s[x])

def enlarge(s:str) :
	while len(s) < 8 :
		s += "Z"
	print(s)

if __name__ == "__main__" :
	if len(sys.argv) < 2 :
		print("none")
	else :
		try:
			for x in sys.argv[1:] :
				if (len(x) > 8) :
					shrink(x)
				else :
					enlarge(x)
		except:
			print("An exception occurred.")
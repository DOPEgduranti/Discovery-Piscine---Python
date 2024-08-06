#!/usr/bin/env python3
import sys
def downcase_it(s:str) -> str :
	return s.lower()

if __name__ == "__main__" :
	if len(sys.argv) < 2 :
		print("none")
	else :
		try:
			for x in sys.argv[1:] :
				print(downcase_it(x))
		except:
			print("An exception occurred.")
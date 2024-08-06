#!/usr/bin/env python3
def upcase_it(s:str) -> str :
	return s.upper()

if __name__ == "__main__" :
	try :
		print(upcase_it("ciao"))
	except:
		print("An exception occurred.")
#!/usr/bin/env python3
def add_one(x) :
	x += 1
	return

if __name__ == "__main__" :
	try:
		x = 7
		print(x)
		add_one(x)
		print(x)
	except:
		print("An exception occurred.")
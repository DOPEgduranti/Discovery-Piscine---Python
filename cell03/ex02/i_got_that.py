#!/usr/bin/env python3
try:
	str = input("What you gotta say? : ").strip()
	while str != "STOP" :
		str = input("I got that! Anything else? : ").strip()
except:
	print("An exception occurred.")
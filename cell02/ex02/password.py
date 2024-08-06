#!/usr/bin/env python3
password = "Python is awesome"
try :
	str = input()
	if str == password :
		print("ACCESS GRANTED")
	else :
		print("ACCESS DENIED")
except:
	print("An exception occurred.")
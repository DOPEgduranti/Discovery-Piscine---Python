#!/usr/bin/env python3
try :
	arr0 = [2, 8, 9, 48, 8, 22, -12, 2]
	arr1 = []
	for x in arr0 :
		if x > 5 :
			arr1.append(x + 2)
	print("Original array:", arr0)
	print("New array:", arr1)
except:
	print("An exception occurred.")
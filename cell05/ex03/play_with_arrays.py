#!/usr/bin/env python3
try :
	arr0 =  [2, 8, 9, 48, 8, 22, -12, 2]
	myset = set(())
	for x in arr0 :
		if x > 5 :
			myset.add(x + 2)
	print(arr0)
	print(myset)
except:
	print("An exception occurred.")
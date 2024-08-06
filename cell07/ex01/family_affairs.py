#!/usr/bin/env python3
def find_the_redheads(d:dict) -> list :
	return list(filter(lambda item: d[item] == "red", d))

if __name__ == "__main__" :
	try:
		dupont_family = {
		"florian": "red",
		"marie": "blond",
		"virginie": "brunette",
		"david": "red",
		"franck": "red"
		}
		print(find_the_redheads(dupont_family))
	except:
		print("An exception occurred.")
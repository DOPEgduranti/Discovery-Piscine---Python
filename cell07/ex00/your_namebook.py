#!/usr/bin/env python3
def array_of_names(d:dict) :
	my_dic = []
	for i in d :
		my_dic.append(i.capitalize() + " " + d[i].capitalize())
	return my_dic

if __name__ == "__main__" :
	try:
		persons = {
		"jean": "valjean",
		"grace": "hopper",
		"xavier": "niel",
		"fifi": "brindacier"
		}
		print(array_of_names(persons))
	except:
		print("An exception occurred.")
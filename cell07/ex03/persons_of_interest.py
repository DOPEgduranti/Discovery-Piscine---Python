#!/usr/bin/env python3
def famous_births(d:dict) :
	date = []
	for x in d :
		date.append(d[x]["date_of_birth"])
	date.sort()
	new_dict = dict()
	for x in date :
		for y in d :
			if d[y]["date_of_birth"] == x :
				new_dict[y] = {"name": d[y]["name"], "date_of_birth": d[y]["date_of_birth"]}
	for x in new_dict :
		print(new_dict[x]["name"], "is a great scientist born in", new_dict[x]["date_of_birth"])
	# new_dict = sorted(d.items(), key = lambda x: x[1]["date_of_birth"])
	# for x in new_dict :
	# 	print(d[x[0]]["name"], "is a great scientist born in", d[x[0]]["date_of_birth"])
	

if __name__ == "__main__" :
	try:
		women_scientists = {
		"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
		"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
		"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
		"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
		}
		famous_births(women_scientists)
	except:
		print("An exception occurred.")
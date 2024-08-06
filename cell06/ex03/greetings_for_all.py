#!/usr/bin/env python3
def greetings(name:str = "noble stranger") :
	if isinstance(name, str) :
		print(f"Hello, {name}.")
	else :
		print("Error! It was not a name.")

if __name__ == "__main__" :
	try:
		greetings('Alexandra')
		greetings('Wil')
		greetings()
		greetings(42)
	except:
		print("An exception occurred.")
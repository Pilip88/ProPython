def add_prefix(string, prefix='pro_'):
	"""Adds a 'pro_' prefix before the string is provided"""
	return prefix + string

mystring = input('Enter a string, so we can put pro_ infront of it: ')
print(add_prefix(mystring))
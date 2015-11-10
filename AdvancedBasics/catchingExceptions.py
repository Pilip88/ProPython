def count_lines(filename):
	"""
	Count the number of lines in a file. If the file can't be
	opened, it should be treated the same as if it was empty.
	"""
	try:
		return len(open(filename, 'r').readlines())
	except:
		# Something went wrong reading the file
		# or calculating the number of lines.
		return 0

myfile = input("Enter a file to open: ")
print(count_lines(myfile))
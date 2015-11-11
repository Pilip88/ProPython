def count_lines(filename):
	"""Count the number of lines in a file"""
	with open(filename, 'r') as file:
		return len(file.readlines())

somefile = input('File to open: ')
print(count_lines(somefile))

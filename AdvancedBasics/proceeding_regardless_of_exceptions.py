import logging

def count_lines(filename):
	"""
	Count the number of lines in a file. If the file can't be
	opened, it should be treated the same as if it was empty.
	"""
	file = None # file must always have a value
	try:
		file = open(filename, 'r')
		lines = file.readlines()
	except TypeError as e:
		# The filename wasn't valid for use with the filesystem.
		logging.error(e)
		return 0
	except EnvironmentError as e:
		# Something went wrong reading the file.
		logging.error(e.args[1])
		return 0
	except UnicodeError as e:
		# The contents of the file were in an unknown encoding.
		logging.error(e)
		return 0
	else:
		return len(lines)
	finally:
		if file:
			file.close()

myfile = input("File to open: ")
print(count_lines(myfile))

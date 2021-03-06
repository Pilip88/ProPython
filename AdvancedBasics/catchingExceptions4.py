import logging

def count_lines(filename):
	"""
	Count the number of lines in a file. If the file can't be
	opened, it should be treated the same as if it was empty.
	"""
	try:
		return len(open(filename, "r").readlines())
	except (EnvironmentError, TypeError) as e:
		# Soething went wrong reading the file.
		logging.error(e)
		return 0

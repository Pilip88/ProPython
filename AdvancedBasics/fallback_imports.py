try:
	# Use the new library if available. Added in Python 2.5
	from hashlib import md5
	print('imported md5 from hashlib')
except ImportError:
	# Compatible functionality provided prior to Python 2.5
	from md5 import new as md5
	print('imported new as md5 from md5')
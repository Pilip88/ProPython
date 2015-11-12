try:
	import docutils # Common Python-based documentation tools
except ImportError:
	docutils = None

if docutils:
	print('docutils!')
else:
	print("I don't have it!")
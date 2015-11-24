class PluginMount(type):
	"""
	Place this metaclass on any standard Python class to turn it into a plugin
	mount point. All subclasses will be automatically registered as plugins.
	"""

	def __init__(cls, name, bases, attrs):
		if not hasattr(cls, 'plugins'):
			# The class has no plugins list, so it must be a mount point,
			# so we add one for plugins to be registered in later.
			cls.plugins = []
		else:
			# Since the plugins attribute already exists, this is an
			# individual plugin, and it needs to be registered.
			cls.plugins.append(cls) 


class InputValidator(metaclass=PluginMount):
	"""
	A plugin mount for input validation.

	Supported plugins must provide a validate(self, input) method, which receives
	input as a string and raises a ValueError if the input was invalid. If the
	input was properly valid, it should return without error. Any return value
	will be ignored.
	"""

	def validate(self, input):
		"""
		The default implementation raises a NonImplementedError
		to ensure that any subclasses must override this method.
		"""
		raise NonImplementedError


class ASCIIValidator(InputValidator):
	"""
	Validate that the input only consists of valid ASCII characters.
	
	>>> v = ASCIIValidator()
	>>> v.validate('sombrero')
	>>> v.validate('валапењо')
	Traceback (most recent call last):
		...
	UnicodeDecodeError: 'ascii' codec can't decode character '' in
	position 6: ordinal not in range(128)
	"""

	def validate(self, input):
		"""
		If the encoding operation fails, str.encode() raises a
		UnicodeDecodeError, which is a subclass od ValueError.
		"""
		input.encode('ascii')


class NoDigitValidator(InputValidator):
	"""
	Validate that the input doesn't contain any digit.
	"""
	def validate(self, input):
		for char in input:
			if char.isdigit():
				raise ValueError


def is_valid(input):
	for plugin in InputValidator.plugins:
		try:
			plugin().validate(input)
		except ValueError:
			# A ValueError means invalid input
			return False
	# All validators succeeded
	return True


print(is_valid('ćžšđ'))
print(is_valid('dfdsfk'))
print(is_valid('343'))
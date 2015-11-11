def test_value(value):
	if value < 100:
		return 'The value is just right.'
	else:
		return 'The value is too big!'

print(test_value(78))
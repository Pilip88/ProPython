def test_value(value):
	return 'The value is ' + ('just right.' if value < 100 else 'too big!')

print(test_value(45))
def echo():
	"""Returns everything you type until you press Ctrl-C"""
	while True:
		try:
			print(input('Type Something or Ctrl-C to exit: '))
		except KeyboardInterrupt:
			print()
			print("bye for now...")
			break

echo()
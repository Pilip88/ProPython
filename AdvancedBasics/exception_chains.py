def get_value(dictionary, name):
	try:
		return dictionary[name]
	except Exception as e:
		print("exception hit...writing to file")
		log = open("logfile.txt", "w")
		log.write("%s\n" % e)
		log.close()

names = {"Jack": 113, "Jill": 32, "Yoda": 396}
print(get_value(names, "Jackzdad"))

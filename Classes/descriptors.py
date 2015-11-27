import datetime

class LoggedAttribute:
	def __init__(self):
		self.log = []
		self.value_map = {}
	def __set__(self, instance, value):
		self.value_map[instance] = value
		log_value = (datetime.datetime.now(), instance, value)
		self.log.append(log_value)
	def __get__(self, instance, owner):
		if not instance:
			return self
		return self.value_map[instance]


class Example:
	value = LoggedAttribute()


e = Example()
e.value = 'testing'
print(e.value)

print(Example.value.log)
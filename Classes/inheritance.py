class Contact:
	def __init__(self, lName, fName): # explicit constructor for class
		self.lastName = lName
		self.firstName = fName

worker1 = Contact('Smith', 'James')

print(worker1.lastName, worker1.firstName) # object.public_property

newLast = input('Enter new last name: ')
setattr(worker1, 'lastName', newLast) # set atribute with new value
print(worker1.lastName, worker1.firstName)
print(getattr(worker1, 'lastName')) # get existing attribute
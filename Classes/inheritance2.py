class Contact:
	name = TextField()
	email = EmailField()
	phone = PhoneNumberField()

	def send_mail(self, message):
		# Email sending code would go here


class Person(Contact):
	first_name = TextField()
	last_name = TextField()
	name = ComputedString('%(last_name)s, %(first_name)s')
	cell_phone = PhoneNumberField()


class Company(Contact):
	industry = TextField()


class Eployee(Person):
	employer = RelatedContact(Company)
	job_title = TextField()
	office_email = EmailField()
	office_phone = PhoneNumberField()
	extension = ExtensionField()


class Friend(Person):
	relationship = TextField()


class FamilyMember(Person):
	relationship = TextField()
	birthday = DateField()

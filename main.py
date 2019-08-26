class Contact:
	def __init__(self, shortname, longname, phone, is_favorite = False, *args, **kwargs):
		self.shortname = shortname
		self.longname = longname
		self.phone = phone
		self.is_favorite = is_favorite
		self.addition_info = args 
		self.addition_info_dict = kwargs
	def __str__(self):
		pass

class PhoneBook():
	def __init__(self, bookname):
		self.bookname = bookname
		self.resultBook = []
	#def __iter__(self):
	#	return self
	#def __next__(self):
	#	return self.resultBook
	def showall(self):
		return self.resultBook
	def add(self, contact_to_add):
		#print('ResultBook before: ', self.resultBook)
		#print('Type Contact to add: ', type(contact_to_add))
		#print('Data Contact to add: ', contact_to_add)
		self.resultBook.append(contact_to_add)
		#print('ResultBook after: ', self.resultBook)
		return self.resultBook
	def remove(self, phone):
		pass
	def fav_search(self):
		pass
	def name_search(self,*args):
		pass

if __name__ == '__main__':
	mycontact01 = Contact('Ivan','Petrov','1230101')
	mycontact02 = Contact('Sergey','Ivanov','1230202')
	print(type(mycontact01))
	print('Name: ',mycontact01.shortname, ' ', mycontact01.longname,' ', mycontact01.phone)
	mycontactbook = PhoneBook('mybook')
	print('My phonebook name: ', mycontactbook.bookname)
	print('My phonebook name: ', mycontactbook.bookname)
	print('My phonebook list: ', mycontactbook.showall())
	mycontactbook.add(mycontact01)
	print('My phonebook list: ', mycontactbook.showall())
	mycontactbook.add(mycontact02)
	print('My phonebook list: ', mycontactbook.showall())
	print('My phonebook type: ', type(mycontactbook))
	print('My phonebook 0: ')
	for elem in mycontactbook.showall():
		print('Shortname:', elem.shortname, ' Longname:', elem.longname, ' phone:', elem.phone, ' Is favorite:', elem.is_favorite)

import itertools

class Contact:
	def __init__(self, shortname, longname, phone, *args, **kwargs, is_favorite = False):
		self.shortname = shortname
		self.longname = longname
		self.phone = phone
		self.is_favorite = is_favorite
		self.addition_info = args 
		self.addition_info_dict = kwargs
	def __str__(self):
		return '%s__%s' % (self.longname, self.shortname)

class PhoneBook():
	def __init__(self, bookname):
		self.bookname = bookname
		self.resultBook = []
		self.idx = 0
	def __iter__(self):
		return self
	def __next__(self):
		self.idx =+ 1
		try:
			return self.resultBook[self.idx - 1]
		except IndexError:
			self.idx = 0
			raise StopIteration

	def return_list(self):
		return self.resultBook
	def show_all(self):
		print('-------Notebook--name---',self.bookname,'-------')
		for elem in self.return_list():
			print('Name:', elem.shortname, ' Longname:', elem.longname, ' Phone:', elem.phone, ' Is favorite:', elem.is_favorite)
	def add(self, contact_to_add):
		#print('ResultBook before: ', self.resultBook)
		#print('Type Contact to add: ', type(contact_to_add))
		#print('Data Contact to add: ', contact_to_add)
		self.resultBook.append(contact_to_add)
		#print('ResultBook after: ', self.resultBook)
		return self.resultBook
	def remove(self, searchphone):
		self.resultBook = itertools.filterfalse(lambda x: x.phone == searchphone, self.resultBook)
		return self.resultBook
	def fav_search(self):
		pass
	def name_search(self,*args):
		pass

if __name__ == '__main__':
	mycontact01 = Contact('Ivan','Petrov','1230101')
	mycontact02 = Contact('Sergey','Ivanov','1230202')
	mycontact03 = Contact('Oleg','Smirnov','0000001', is_favorite = True, 'nothome','Kostroma',email='olegsmirnov@kostroma.ru')
	#print(type(mycontact01))
	#print('Name: ',mycontact01.shortname, ' ', mycontact01.longname,' ', mycontact01.phone)
	mycontactbook = PhoneBook('mybook')
	#print('My phonebook list: ', mycontactbook.show_all())
	#mycontactbook.add(mycontact01)
	#print('My phonebook list: ', mycontactbook.show_all())
	mycontactbook.add(mycontact02)
	mycontactbook.add(mycontact03)
	print('My phonebook list: ', mycontactbook.show_all())
	print('My phonebook type: ', type(mycontactbook))
	print('My phonebook 0: ', next(mycontactbook))

	#mylist = ['ivanov','petrov','sidorov']
	#print('mylist filtered',list(itertools.filterfalse(lambda x: x == 'sidorov', mylist)))

	for elem in mycontactbook.return_list():
		print('Shortname:', elem.shortname, ' Longname:', elem.longname, ' phone:', elem.phone, ' Is favorite:', elem.is_favorite, 'Addition info:', elem.addition_info, ' Addition info2:', elem.addition_info_dict)

















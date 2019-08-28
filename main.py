import itertools

class Contact:
	def __init__(self, shortname, longname, phone, *args, is_favorite = False, **kwargs):
		self.shortname = shortname
		self.longname = longname
		self.phone = phone
		self.is_favorite = is_favorite
		self.addition_info = args 
		self.addition_info_dict = kwargs
		self.args = args
		self.kwargs = kwargs
	def __str__(self):
		print('Имя:', self.shortname)
		print('Фамилия:', self.longname)
		print('Телефон:', self.phone)
		if self.is_favorite:
			print('В избранных: да')
		else:
			print('В избранных: нет')
		print('Дополнительная информация:')
		if self.args:
			for elem in self.args:
				print('\t\t', elem)
		if self.kwargs:
			for elem in self.kwargs:
				print('\t\t', elem)
		return '%s_%s' % (self.longname, self.shortname)

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
		self.resultBook.append(contact_to_add)
		return self.resultBook
	def remove(self, searchphone):
		self.resultBook = itertools.filterfalse(lambda x: x.phone == searchphone, self.resultBook)
		return self.resultBook
	def fav_search(self):
		k = 0
		for elem in self:
			k += 1
	def name_search(self,*args):
		pass

if __name__ == '__main__':
	mycontact01 = Contact('Ivan','Petrov','1230101')
	mycontact02 = Contact('Sergey','Ivanov','1230202')
	jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
	print(jhon)
	mycontact03 = Contact('Oleg','Smirnov','0000001', 'nothome','Kostroma', is_favorite = False ,email='olegsmirnov@kostroma.ru')
	mycontactbook = PhoneBook('mybook')
	mycontactbook.add(mycontact02)
	mycontactbook.add(mycontact03)
	print('My phonebook list: ', mycontactbook.show_all())
	print('My phonebook type: ', type(mycontactbook))
	print('My phonebook 0: ', next(mycontactbook))
'''
	for elem in mycontactbook.return_list():
		print('Shortname:', elem.shortname, ' Longname:', elem.longname, ' phone:', elem.phone, ' Is favorite:', elem.is_favorite, 'Addition info:', elem.addition_info, ' Addition info2:', elem.addition_info_dict)
'''
















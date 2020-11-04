class Employee :
	
	def __init__(self, first_name, last_name, salary) :
		self.__first_name = first_name
		self.__last_name = last_name
		self.__salary = salary
	
	def get_first(self) :
		return self.__firstname
	
	def get_last(self) :
		return self.__lastname
	
	def get_salary(self) :
		return self.__salary
	
	def give_raise(self, amount=0.02) :
		self.__salary *= (1.00+amount)
	

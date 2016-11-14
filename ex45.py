##Animal is-a object
class Animal(object):
	def __init__(self,atype):
		self.atype= atype

##dog is-a animal
class Dog(Animal):
	def __init__(self,name,atype):
		self.name=name
		super(Dog,self).__init__(atype)

##cat is-a animal
class Cat(Animal):
	def __init__(self,name,atype):
		self.name=name
		super(Cat,self).__init__(atype)

#person is-a object
class Person(object):
	def __init__(self,name):
		self.name=name
		self.pet=None

#employee is-a peson
class Employee(Person):
	def __init__(self,name,salary):
		super(Employee,self).__init__(name)
		self.salary=salary

#Fish is-a object
class Fish(object):
	pass

#salmon is-a fish
class Salmon(Fish):
	pass

#halibut is-a fish
class Halibut(Fish):
	pass

#rover is-a dog
rover=Dog("Rover",'wild')

# #satan is-a cat
# satan=Cat("Satan")

# #mary is-a person
# mary=Person("Mary")

# #mary has-a satan
# mary.pet=satan

# #frank is-a employee
# frank=Employee("Frank",120000)

# #frank has-a rover
# frank.pet=rover

# #flipper is-a fish
# flipper=Fish()

# #crouse is-a salmon
# crouse=Salmon()

# #harry is-a halibut
# harry=Halibut()
class Person:
	'''Represents a person.'''
	population = 0
	def _init_(self, name):
		'''Initializes the person's data.'''
		self.name = name
		print('(Initializing %s)' % self.name)
		Person.population += 1	
	def _del_(self):
		'''I am dying'''
		print('%s says bye.' % self.name)	
		Person.population -= 1
		if Person.population == 0:
			print('I am the last one.')
		else:
			print('There are still %d people left.' % Person.population)
	def sayHi(self):
		'''Greeting by the Person.
		Really, that's all it does.'''
		print('Hi, my name is %s' % self.name)
	def howMany(self):
		'''print the current population.'''
		if Person.population == 1:
			print('I am the only person here.')
		else:
			print('we have %d persong here.' % Person.population)	

swaroop = Person('Swaroop')				
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()
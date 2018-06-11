# 使用_init_方法
class Person:
	def _init_(self,name):
		self.name = name
	def sayHi(self):
		print('hello, my name is', self.name)

p = Person('Swaroop')
p.sayHi()
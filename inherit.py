class  SchoolMember():
	"""docstring for  SchoolMember"""
	''' 代表了任何学校成员'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
	print('Initialized SchoolMember: %s' % self.name)
	def tell(self):
		''' 告诉我详细的情况'''
		print("Name:'%s' Age:'%s' % (self.name, self.age)"),
class Teacher(SchoolMember):
	"""docstring for Teacher"""
	''' 代表了一个老师'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('Initialized teacher: %s' % self.name)

	def tell(self):
		SchoolMember.tell(self)
		print('salary: %d' % self.salary)

class Student(SchoolMember):
	"""docstring for Student"""
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Initialized student: %s' % self.name)
	def tell(self):
		SchoolMember.tell(self)
		print('marks: %d' % self.marks)

t = Teacher('Mrs.Shaquin', 40, 30000)
s = Student('Swaroop', 22, 75)
print()
members = [t, s]
for  member in members:
	 member.tell()
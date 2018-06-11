# 创建一个类
class Person:  # 注意：这里没有缩进
 	pass	   # 一个空白语句块，承接上面的缩进语句：
p = Person()   # 注: 这块儿也没有缩进
print (p)      # print后面要有双括号“（）” ，这接打print p 是不正确的

# 使用对象的方法
class Person:
	def sayhello(self):  # 注意:类的方法（不同于单纯的函数）中含有一个额外的 self 变量
		print('Hello, unnatural is a good Japanese drama')  # 这是包含在定义Person类缩进中的语句块，不是单纯的print打印
p = Person()
p.sayhello()	# 如果没有这句对象调用函数的方法，无法打印出来
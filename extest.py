from random import randint
class A(object):

	def __init__(self):
		a=['1','2','3','4','5']
		self.b=a[randint(0,len(a)-1)]
		print self.b

q=A()
w=A()
q=A()
w=A()
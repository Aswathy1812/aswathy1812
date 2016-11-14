class Thing(object):
	
	def __init__(self):
		self.number=0

	def addmore(self,num):
		self.number+=num
		return self.number

	def display(self):
		print self.number

	def check(self):
		return 'abc'
	
	def abc(self):
		print "Yes!"
		return 2

	def test(self):
		print "----"
		t='check'
		x=getattr(self,t)
		print x
		t=x()
		x=getattr(self,t)
		print '----',x
		u=x()
		print u

a=Thing()
b=Thing()
print "number"
print a.number
print b.number

res=a.addmore(10)
res=a.addmore(20)

print "display a"
a.display()
print "res"
print res

print "display b"
res=b.addmore(50)
b.display()
print "----"
print a.number
print b.number
c=Thing()
c.test()
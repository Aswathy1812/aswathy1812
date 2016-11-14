from sys import exit
class room(object):
	def __init__(self,start):
		self.start=start

	def living(self):
		print "You can sit here.."
		print "Are you hungry?(y/n)"
		hungry=raw_input("> ")

		if hungry=='y':
			return 'dining'

		else:
			return 'living'

	def dining(self):
		print "Have food here.."
		print "Are you sleepy?(y/n)"
		sleepy=raw_input("> ")

		if sleepy=='y':
			return 'bedroom'
		else:
			return 'dining'

	def bedroom(self):
		print "You can sleep here.."
		print "Do you want to leave?(y/n)"
		leave=raw_input("> ")

		if leave=='y':
			return 'goback'
		else:
			return 'bedroom'

	def goback(self):
		print "You are free to go any where..bye!"
		exit(1)

class visit(room):
	def welcome(self,ob):
		#self.start=start
		next=ob.start

		while True:
			rm=getattr(self,next)
			next=rm()


ob1=room('living')
ob2=visit(ob1)
ob2.welcome(ob1)



from sys import exit
class home(object):
	def __init__(self):
		
		print "Welcome home.."
		print "Please come inside.." 

	def hungry(self):
		print "Are you hungry?(y/n)"
		self.hunger=raw_input("> ")
		

	def sleepy(self):
		print "Are you sleepy?(y/n)"
		self.sleepy=raw_input("> ")
		

	def going(self):
		print "Are you leaving?(y/n)"
		self.leave=raw_input("> ")
		
	def relax(self):
		print "You may relax for some more time..."
		raw_input()

	def host(self):
		while True:
			l=living()
			l.explain()
			#if l.choice=='stand'
			self.hungry()
			if (self.hunger=='y'):
				d=dining()
				d.explain()
				
			self.sleepy()
			if (self.sleepy=='y'):
				b=bedroom()
				b.explain()
				
			self.going()
			if(self.leave=='y'):
				print "Bye... come again!"
				exit(1)
			else:
				self.relax()
				self.going()
				if(self.leave=='y'):
					print "Bye... come again!"
					exit(1)
				else:
					print "sorry timed out!.. you should leave now! "
					exit(1)




class living(object):
	def __init__(self):
		self.colour='pink'
		self.door=2
		self.window=3

	def explain(self):
		print "This is the Living room"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "There is a chair..\n.sit\n.open the door"
		#self.choice=(raw_input("> "))

class dining(object):
	def __init__(self):
		self.colour='blue'
		self.door=3
		self.window=4
	
	def explain(self):
		print "This is the Dining room"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "Please sit down and have some food..\n.eat\n.dont eat"
		#self.choice=raw_input("> ")

class bedroom(object):
	def __init__(self):
		self.colour='white'
		self.door=1
		self.window=2
	
	def explain(self):
		print "This is the Bedroom"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "Please lie down n take rest..\n.lie down\n.dont lie down"
		#self.choice=raw_input("> ")


h=home()
h.host()
	

	


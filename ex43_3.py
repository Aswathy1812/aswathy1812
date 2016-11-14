from sys import exit
class home(object):
	def __init__(self):
		
		print "Welcome home.."
		print "Please come inside.." 
		raw_input()

	def host(self):
		l=living()
		l.explain()
		l.trick()

class living(object):
	def __init__(self):
		self.colour='pink'
		self.door=2
		self.window=3

	def explain(self):
		print "This is the Living room"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "There is a chair..\n.sit\n.open the door"
		self.choice=(raw_input("> "))
	def trick(self):
		if self.choice=='sit':
			print "The chair breaks.. u fall down..You lose"
			exit(1)
		elif self.choice=='open the door':
			print "Good choice!.."
			d=dining()
			d.explain()
			d.trick()
		else:
			print "bad choice!.."
			self.explain()
			self.trick()

class dining(object):
	def __init__(self):
		self.colour='blue'
		self.door=3
		self.window=4
	
	def explain(self):
		print "This is the Dining room"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "Please sit down and have some food..\n.eat\n.dont eat"
		self.choice=raw_input("> ")
	def trick(self):
		if self.choice=='eat':
			print "good choice.."
			b=bedroom()
			b.explain()
			b.trick()
		elif self.choice== 'dont eat':
			print "A beast appears from nowhere n eats u up!!...you lose!"
			exit(1)
		else:
			print "bad choice!.."
			self.explain()
			self.trick()

class bedroom(object):
	def __init__(self):
		self.colour='white'
		self.door=1
		self.window=2
	
	def explain(self):
		print "This is the Bedroom"
		print "This is a ",self.colour," room with ",self.door," doors and ",self.window," windows."
		print "Please lie down n take rest..\n.lie down\n.dont lie down"
		self.choice=raw_input("> ")
	def trick(self):
		if self.choice== 'lie down':
			print "You get lost in dreams forever!..you lose!"
			exit(1)
		elif self.choice=='dont lie down':
			print "A magic door opens...u may escape..You win!Congrats!."
			exit(1)
		else:
			print "bad choice!.."
			self.explain()
			self.trick()

h=home()
h.host()
	

	


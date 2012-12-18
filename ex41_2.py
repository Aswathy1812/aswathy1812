from sys import exit
from random import randint

def death():
	quips = ["You died. You are bad at this.",
             "Your mom would be proud. If she were smarter.",
             "Such a loser.",
             "I have a small puppy that's better at this."]
    
	print quips[randint(0, len(quips)-1)]
	exit(1)

def princess_lives_here(eat_it):
	
	"""You see a beautiful Princess with a shiny crown.
	   She offers you some cake.
	    .eat it
		.do not eat it
		.make her eat it"""

	if eat_it == "eat it":
		print "You explode like a pinata full of frogs."
		print "The Princess laughs and eats the frogs. Yum!"
		print "\n-----------------\n"
		death()

	elif eat_it == "do not eat it":
		print "She throws the cake at you and it cuts off your head."
		print "The last thing you see is her munching you. Yum!"
		print "\n-----------------\n"
		death()

	elif eat_it == "make her eat it":
		print "The Princess screams as you cram the cake in her mouth."
		print "Then she smiles and cries and thanks you for saving her."
		print "She points to a tiny door and says, 'The Koi needs cake too.'"
		print "She gives you the very last bit of cake and shoves you in."
		print "\n-----------------\n"
		print gold_koi_pond.__doc__
		gold_koi_pond(raw_input("> "))

	else:
		print "The princess looks at you confused and just points at the cake."
		print "\n-----------------\n"
		print princess_lives_here.__doc__
		princess_lives_here(raw_input("> "))



def gold_koi_pond(feed_it):
	
	"""There is a garden with a koi pond in the center.
	You walk close and see a massive fin poke out.
	You peek in and a creepy looking huge Koi stares at you.
	It opens its mouth waiting for food.
		.feed it
		.do not feed it
		.throw it in"""
	if feed_it == "feed it":
		print "The Koi jumps up, and rather than eating the cake, eats your arm."
		print "You fall in and the Koi shrugs than eats you."
		print "You are then pooped out sometime later."
		print "\n-----------------\n"
		death()

	elif feed_it == "do not feed it":
		print "The Koi grimaces, then thrashes around for a second."
		print "It rushes to the other end of the pond, braces against the wall..."
		print "then it *lunges* out of the water, up in the air and over your"
		print "entire body, cake and all."
		print "You are then pooped out a week later."
		print "\n-----------------\n"
		death()

	elif feed_it == "throw it in":
		print "The Koi wiggles, then leaps into the air to eat the cake."
		print "You can see it's happy, it then grunts, thrashes..."
		print "and finally rolls over and poops a magic diamond into the air"
		print "at your feet."
		print "\n-----------------\n"
		print bear_with_sword.__doc__
		bear_with_sword(raw_input("> "))

	else:
		print "The Koi gets annoyed and wiggles a bit."
		print "\n-----------------\n"
		print gold_koi_pond.__doc__
		gold_koi_pond(raw_input("> "))

		

def bear_with_sword(give_it):
	
	"""Puzzled, you are about to pick up the fish poop diamond when
	a bear bearing a load bearing sword walks in.
	'Hey! That\'s my diamond! Where\'d you get that!?'
	It holds its paw out and looks at you.
	
		.give it
		.say no"""
	
	if give_it == "give it":
		print "The bear swipes at your hand to grab the diamond and"
		print "rips your hand off in the process. It then looks at"
		print 'you and says, "Oh crap, sorry about that."'
		print "It tries to put your hand back on, but you collapse."
		print "The last thing you see is the bear shrug and eat you."
		print "\n-----------------\n"
		death()

	elif give_it=="say no":
		print "The bear looks shocked. Nobody has ever told a bear"
		print "with a broadsword 'no'. It asks, "
		print '"Is it because it\'s not a katana? I could go get one!"'
		print "It then runs off and now you notice a big iron gate."
		print  '"Where the hell did that come from?"You say.'
		print"\n-----------------\n"
		print big_iron_gate.__doc__
		big_iron_gate(raw_input("> "))

	else:
		print "The bear look puzzled as to why you'd do that."
		print "\n-----------------\n"
		print bear_with_sword.__doc__
		bear_with_sword(raw_input("> "))

def big_iron_gate(open_it):
	

	"""You walk up to the big iron gate and see there's a handle.
		.open it"""

	if open_it=='open it':
		print "You open it and you are free!"
		print "There are mountains. And berries! And..."
		print "Oh,but then the bear comes with his katana and stabs you."
		print '"Who\'s laughing now!? Love this katana."'
		print "\n-----------------\n"
		death()

	else:
		print "That doesn't seem sensible. I mean, the door's right there."
		print "\n-----------------\n"
		print big_iron_gate.__doc__
		big_iron_gate(raw_input("> "))
	



def runner():
	princess_lives_here(raw_input("> "))

print princess_lives_here.__doc__
runner()




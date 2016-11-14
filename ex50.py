from sys import exit
l=0
res=[]
import string
def convert_number(s):
	try:
		return int(s)
	except ValueError:
		return None

def scan(stuff):
	stuff=string.lower(stuff)
	words=stuff.split(' ')
	direction=('north','south','east','west','up','down','left','right','back','forward','through','there','near','across','away')
	verbs=('go','stop','kill','eat','kick','climb','beat','walk','open','move','feed','run','stand','throw','shout','jump')
	stop=('the','in','of','from','at','it','to','into')
	nouns=('door','bear','princess','fast','rock','swan','bridge','tunnel','fish','key','river','alien','quietly','cattle','slowly','still')
	global l,res
	res=[]
	l=len(words)
	for i in range(l):
		if words[i] in direction:
			res.append(('direction',words[i]))
		elif words[i] in verbs:
			res.append(('verb',words[i]))
		elif words[i] in stop:
			res.append(('stop',words[i]))
		elif words[i] in nouns:
			res.append(('noun',words[i]))
		elif convert_number(words[i]):
			res.append(('number',int(words[i])))
		else:
			res.append(('error',words[i]))
	return res

class ParseError(Exception):
	pass

class Sentence(object):
	
	def __init__(self, subject, verb, object):
		# remember we take ('noun','princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]

class InputSentence(object):
	#returns first word of the word_list
	def peek(self,word_list):
		if word_list:
			word = word_list[0]
			return word[0]
		else:
			return None
	#checks if the encountered word is the expected word
	def match(self,word_list, expecting):
		if word_list:
			word = word_list.pop(0)
			if word[0] == expecting:
				return word
			else:
				return None
		else:
			return None

	def skip(self,word_list, word_type):
		while self.peek(word_list) == word_type:
			self.match(word_list, word_type)

	def parse_verb(self,word_list):
		self.skip(word_list, 'stop')
		if self.peek(word_list) == 'verb':
			return self.match(word_list, 'verb')
		else:
			raise ParseError("Expected a verb next.")

	def parse_object(self,word_list):
		self.skip(word_list, 'stop')
		next = self.peek(word_list)
		if next == 'noun':
			return self.match(word_list, 'noun')
		if next == 'direction':
			return self.match(word_list, 'direction')
		else:
			raise ParseError("Expected a noun or direction next.")
			
	def parse_subject(self,word_list, subj):
		verb = self.parse_verb(word_list)
		obj = self.parse_object(word_list)
		return Sentence(subj, verb, obj)

	def parse_sentence(self,word_list):
		self.skip(word_list, 'stop')
		start = self.peek(word_list)
		if start == 'noun':
			subj = self.match(word_list, 'noun')
			#print subj
			return self.parse_subject(word_list, subj)
		elif start == 'verb':
			# assume the subject is the player then
			return self.parse_subject(word_list, ('noun', 'player'))
		else:
			raise ParseError("Must start with subject, object, or verb not: %s" % start)

class Mainroom(object):
	def __init__(self):
		self.explain="""
		You are being held captive in an Alien space ship...
		
		You must try to escape from here...
		Try to find a key to open the room 
		
		An Alien is guardingthe cell 
		There are two doors guarded by aliens..
		You can choose one door
		.go north to door 1
		.go east to door 2"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		#print self.choice
		self.trick()

	def trick(self):
		if self.object== 'north':
			l=River()
		elif self.object== 'east':
			f=Farm()
		else:
			m=Mainroom()

class River(object):
	def __init__(self):
		self.explain=""" 
		You keep running through the tunnel...
		Watchout for lasers...

		After running for hours...
		You see a very beautiful River...
		There is a swan at the banks of the river...
		There is a bridge across the river...
		"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		self.trick()
	def trick(self):
		if self.verb in ('walk','go','move') and self.object=='swan':
			s=Swan()
		elif self.verb in ('walk','go','move','climb','run') and self.object=='bridge':
			print "You decide to run...on the way "
			print "You see a tree"
			print "You rest under the tree n when you open your eyes..."
			print "You see a key lying near you.."
			print "You pick up the key and keep it safe.."
			print "Then you continue running...n finally reach the bridge"
			print "You kepp running across the bridge"
			r=Bridge()
		else:
			l=River()

class Farm(object):
	def __init__(self):
		self.explain="""
		There is a farm with a lot of crops...
		
		You run through the field n destroy the crops...
		The aliens get angry and start firing laser beams..
		You somehow manage to escape n then you see a door..

		Inorder to open the door you should know the secret code...
		You have three guesses..it is a 3 digit code
		"""
		print self.explain
		self.trick()
	def trick(self):
		for i in range(3):
			print "chance #",i+1,": "
			self.choice=raw_input("> ")
			if self.choice=='000':
				print "The door opens..."
				c=Cattle()
				break
		print "Your chances are over.."
		print "You stand there thinking what to do next..."
		print "Then you walk forward n reach the top of a small hill.."
		print "Suddenly somebody pushes you and you fall down unconscious.. "
		print "Later when you open your eyes..."
		p=Pond()

class Pond(object):
	def __init__(self):
		self.explain="""
		You see a small pond..
		There are a lot of fishes in the pond...
		The fishes need food..You can feed the fishes if u want..
		Aliens are following you...!
		"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		self.trick()
	def trick(self):
		if self.verb=='feed':
			print "You keep feeding the fishes and forget about the aliens"
			print "The aliens catch you and take you with them..."
			l=Lose()
		elif self.verb in ('run','move','walk'):
			print "You see a bridge and run towards it.."
			print "The bridge is built across a river"
			print "On the way you find a key on the ground.."
			print "You pick up the key and run across the bridge..."
			b=Bridge()
		else:
			Pond()

class Cattle(object):
	def __init__(self):
		self.explain="""
		Cattles are grazing...
		You cannot harm the cattle.. aliens are guarding them
		If the aliens notice you,they'll shoot you...
		Either stand still ,walk slowly or shout at the cattle...
		"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		self.trick()
	def trick(self):
		if self.verb in ('walk','run','move','stand') :
			print "A bird is flying above, it drops a key which falls on your head..\nYou pick up the key"
			print "and start running..."
			print "You see a bridge and run towards it.."
			print "The bridge is built across a river"
			print "You run through the bridge..."
			b=Bridge()
		elif self.verb =='shout':
			print "The aliens see you...!"
			print "They come after you.."
			print "You start running for your life"
			print "You hide among the bushes.."
			print "At a distance you see a swan.."
			s=Swan()
		else:
			c=Cattle()

class Bridge(object):
	def __init__(self):
		self.explain="""
		The aliens see you walking through the bridge..
		They come after you and start firing laser...
		You keep running...And collect stones while running..
		And throw them at the aliens..
		Luckily u find a gun on your way..
		You pick up the gun and start shooting the aliens..
		At the other bank you see a spaceship...
		You can either run across or jump into river n swim across..
		"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		self.trick()
	def trick(self):
		if self.verb=='run' :
			print "You get shot in your leg.."
			print "You somehow manage to run across and reach the spaceship.."
			print "You open its door using the key.."
			print "You get inside and get back to earth..."
			w=Win()
		elif self.verb=='jump' :
			print "You try hard to swim across..."
			print "You get caught in the water currents...and lose the key!"
			l=Lose()
		else:
			r=Bridge()

class Swan(object):
	def __init__(self):
		self.explain="""
		As you go near the swan...
		The swan drops a key and flies away...
		On seeing the swan fly , aliens come to attack you...
		You can either throw the key at the aliens and 
		take a chance or keep running!"""
		print self.explain
		self.choice=raw_input("> ")
		ip=InputSentence()
		stuff=self.choice
		result=scan(stuff)
		syntax=ip.parse_sentence(result)
		print syntax.subject," ",syntax.verb," ",syntax.object
		self.choice=syntax.verb + " "+ syntax.object
		self.verb=syntax.verb
		self.object=syntax.object
		print self.choice
		self.trick()
	def trick(self):
		if self.verb=='throw' :
			print "The key was your only chance to escape..."
			l=Lose()
		elif self.verb=='run' :
			print "You see a bridge and run towards it.."
			print "The bridge is built across a river"
			print "You run through the bridge..."
			b=Bridge()
		else:
			s=Swan()

class Win(object):
	def __init__(self):
		print "Luckily you had the key!"
		self.explain="""You Win!"""
		print self.explain
		exit(1)

class Lose(object):
	def __init__(self):
		self.explain="""You Lose!"""
		print self.explain
		exit(1)

m=Mainroom()

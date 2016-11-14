
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
	direction=('north','south','east','west','up','down','left','right','back','forward','through','to')
	verbs=('go','stop','kill','eat','kick','beat','walk','open')
	stop=('the','in','of','from','at','it')
	nouns=('door','bear','princess','cabinet')
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
			print self.match(word_list, word_type)

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
			print subj
			return self.parse_subject(word_list, subj)
		elif start == 'verb':
			# assume the subject is the player then
			return self.parse_subject(word_list, ('noun', 'player'))
		else:
			raise ParseError("Must start with subject, object, or verb not: %s" % start)

ip=InputSentence()
#stuff=raw_input("> ")
#stuff="kill the bear"
#stuff="north go"
#result=scan(stuff)
#print "result= ",result
# syntax=parse_sentence(result)
# print syntax.subject," ",syntax.verb," ",syntax.object
#syntax=ip.parse_sentence(result)
#print syntax.subject," ",syntax.verb," ",syntax.object

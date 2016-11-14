l=0
res=[]
import string
# def convert_number(s):
# 	try:
# 		return int(s)
# 	except ValueError:
# 		return None
def space(st):
	s1=''
	l=len(st)
	for i in range(l):
		s1+=st[i]
		s1+=' '
	return s1
def isnum(s):
	inp=s.split(' ')
	l=len(inp)
	flag=True
	for i in range(l-1):
		flag=inp[i].isdigit()
		if not flag:
			return False
	return True
def scan(stuff):
	stuff=string.lower(stuff)
	words=stuff.split(' ')
	direction=('north','south','east','west','up','down','left','right','back','forward','through','to')
	verbs=('go','stop','kill','eat','kick','beat','walk')
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
		elif isnum(space(words[i])):
			res.append(('number',(words[i])))
		else:
			res.append(('error',words[i]))
	return res
stuff=raw_input("> ")
result=scan(stuff)
print result
for i in range(l):
	print res[i]





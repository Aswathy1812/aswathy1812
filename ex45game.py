from sys import exit
from random import randint
cows=[]
bulls=[]
def repeat(s):
	t=s.split(' ')
	l=len(t)
	for i in range(l):
		j=0
		while(j<l):
			if t[i]== t[j] and i!=j:
				return False
			j=j+1
	return True

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

def isrange(n):

	nu=int(n)
	chk=True
	if(nu>9999 or nu<1000):
		chk=False
	return chk

def inputcheck(n):
	flag=True
	x=isnum(n)
	s=space(n)

	if  n=='':
		print "\n\t\t\tValue error!"
		return False
	elif  not isnum(s):
		print "\n\t\t\tShould be a number!"
		return False
	elif not isrange(n):
		print "\n\t\t\tShould be a four digit number!"
		return False
	elif not repeat(s):
		print "\n\t\t\tRepeating digits should not be there!"
		return False
	else:
		return True

class Question(object):
	def __init__(self):
		self.explain="""
		****COWS AND BULLS****\n
		Find the number!
		Is is a four digit number...
		There are no repeating digits...
		It contains digits from 0 to 9...

		You have 7 chances
		If your guess has:
		
		COWS-digits present anywhere other than the correct position
		BULLS-digits present at the correct position

		Are you ready?"""

#****************************************************
		n=range(3040,9999)
		num=[]
		ln=len(n)
		for j in range(ln):
			st=str(n[j])
			num.append(space(st))
		l=len(num)
		res=[]
		j=0
		for i in range(l):
			stat=repeat(num[i])
			if stat:
				res.append(num[i])
				j+=1

		self.quest=res
		self.numb=self.quest[randint(0,len(self.quest)-1)]
		print self.explain
		print "\n\t\tEnter any 4 digit number\n"
		print "\n\t\t* * * *"
		#print "\n",self.numb,"\n"
		self.cows=0
		self.bulls=0

#*****************************
	def  check(self,gs):
		self.new=self.numb.split(' ')
		self.cows=0
		self.bulls=0
		global cows,bulls
		for i in range(4):
			if self.new[i]==gs[i]:
				self.bulls+=1
		if self.bulls==4:
			print "\n\t\t\tRight Answer!"
			print "\n\t\t\t  You win!..\n"
			print "\t\t\t*************"
			print "\n\t\t\tPlay Again?(y/n)"
			again=raw_input("\n\t\t\t>")
			if again=='y' or again=='yes' or again=='Y':
				q=Question()
				q.runner()
			else:
				exit(1)
		for i in range(4):
			for j in range(4):
				if gs[i]==self.new[j] and (i!=j):
					self.cows+=1
		
		print "\n\t\t\t",self.bulls," Bulls and ",self.cows," Cows"
		cows.append(self.cows)
		bulls.append(self.bulls)
	def answer(self):
		print self.numb
		print "\n\t\t\tPlay Again?(y/n)"
		again=raw_input("\n\t\t\t>")
		if again=='y' or again=='yes' or again=='Y':
			q=Question()
			q.runner()
		else:
			exit(1)


	def runner(self):
		guess=[]
		global cows,bulls
		cows=[]
		bulls=[]
		for i in range(7):
			
			chk=True
			print "\nChance #",i+1,":",
			n=raw_input(" ")
			chk=inputcheck(n)
			s=space(n)
			while not chk:
				
				print "\nEnter once more.."
				print "\nChance #",i+1,":",
				n=raw_input(" ")
				chk=inputcheck(n)
				s=space(n)
				
			inp=s.split(' ')
			guess.append(s)
			
			self.check(inp)
			print "\nYour guesses:"
			
			for i in range(len(guess)):
				print guess[i],"\t",bulls[i],"B  ",cows[i],"C"

		print "\n\t\t\tYou lose..\n\n\t\t\tThe answer is: ",
		self.answer()


q=Question()
q.runner()






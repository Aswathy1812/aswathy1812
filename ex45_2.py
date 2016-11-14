from sys import exit
from random import randint
#print quips[randint(0, len(quips)-1)]
# limit=(0,1,2,3)
# chances=(0,1,2)
class Question(object):
	def __init__(self):
		self.explain="""
		****COWS AND BULLS****\n
		Try to solve this puzzle...\n
		This is a four digit number...
		There are no repeating digits...
		It contains only digits from 1 to 9...
		Can you guess? You have 7 chances"""
		self.quest=['1 2 3 4','5 4 3 6','8 7 4 9','9 2 3 1','3 2 9 7','4 7 9 2','5 6 7 8','7 9 3 5']
		self.numb=self.quest[randint(0,len(self.quest)-1)]
		print self.explain
		print "\n\t\tEnter any 4 digit number\n"
		print "\n\t\t* * * *"
		print "\n",self.numb,"\n"
		# self.numb='1 2 3 4'
		self.cows=0
		self.bulls=0

	def  check(self,gs):
		self.new=self.numb.split(' ')
		self.cows=0
		self.bulls=0
		
		# print "cows= ",self.cows
		# print "bulls= ",self.bulls
		# print "new= ",self.new
		print "> ",gs
		for i in range(4):
			if self.new[i]==gs[i]:
				self.bulls+=1
		if self.bulls==4:
			print "You win.."
			exit(1)
		for i in range(4):
			for j in range(4):
				if gs[i]==self.new[j] and (i!=j):
					self.cows+=1
		print self.bulls," Bulls and ",self.cows," Cows"
	def answer(self):
		print self.numb

q=Question()
guess=['','','','','','','']
for i in range(7):
	print "Chance #",i+1,":"
	s=""
	d=0
	
	n=int(raw_input("> "))
	while(n>0):
		r=n%10
		d=d*10+r
		n=n/10

	while(d>0):
		r=d%10
		s+=str(r)
		s+=" "
		d=d/10

	# print "num is",s
	inp=s.split(' ')
	
	guess[i]=s
	print "Your input:",guess
	q.check(inp)

print "You lose..\nThe answer is: "
q.answer()








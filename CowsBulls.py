import random
class Helpers(object):
	def __init__(self):
		pass

	def getAnyRandom(self):
		question_option = random.randint(1023,9876)
		digits_in_number = [] 
		for i in str(question_option):
			digits_in_number.append(i)
		return digits_in_number

	def hasRepeating(self, option):
		for i in option:
			count = -1
			for j in option:
				if i==j:
					count +=1
			if count > 0:
				return True
		return False

	def checkInput(self, option):
		for i in option:
			try:
				int(i) 
			except:
				print "\tMust contain only numbers"
				return False
		if len(''.join(option)) != 4 :
			print "\tMust be a 4 digit number"
			return False
		if self.hasRepeating(option):
			print "\tRepetition not allowed"
			return False
		return True

	def getAnOption(self):
		got_option = False
		while not got_option:
			option = self.getAnyRandom()
			if not self.hasRepeating(option):
				got_option =True
		return option

	def exactPosition(self):
		count = 0
		for i in range(4):
			if self.question[i] == self.guess[i]:
				count += 1
		return count

	def hasOccurence(self):
		count = 0
		for i in range(4):
			for j in range(4):
				if self.guess[i] == self.question[j] and i != j:
					count += 1
		return count


class CowsAndBulls(Helpers):
	def __init__(self):
		self.explain="""
			****WELCOME TO COWS AND BULLS****\n
			
			Find the number!
			
			It is a four digit number...
			There are no repeating digits...
			It contains digits from 0 to 9...

			You have 7 chances to guess.
			You may start with a wild guess or may be an intelligent one!
			If your guess has:
			
			COWS - digits present anywhere other than the correct position
			BULLS - digits present at the correct position

			For example, Suppose the actual number is 9872

					and your guess is 7962 , (a wild guess!)

					then the clue is :
						
						BULLS  1 , COWS  2

			Here, we begin!
			"""

		self.question = self.getAnOption()
		self.cows = 0
		self.bulls = 0
		self.guess = []
		print self.explain
		self.runner()




	def processInput(self):
		self.cows = self.hasOccurence()
		self.bulls = self.exactPosition()
		if self.bulls == 4:
			print  'Right Answer! You win'
			self.continueGame()
		else:
			print "\tBULLS: ",self.bulls,
			print "  COWS: ",self.cows

	def processChoice(self, choice):
		continue_choices = ['y','yes','1']
		exit_choices = ['n','no','0']
		accepted_choices = continue_choices + exit_choices
		if choice.lower() in accepted_choices:
			if choice.lower() in continue_choices:
				return 'y'
			else:
				return 'n'
		else:
			return None


	def continueGame(self):
		print "\nDo you want to continue?(Y/N)",
		choice = self.processChoice(raw_input(": "))
		if choice == 'y':
			print "\n\t\t\t\t\tNEXT ROUND\n"
			self.runner()
		elif choice == 'n':
			exit(1)
		else:
			print "Choice cannot be accepted"
			self.continueGame();

	def runner(self):
		for i in range(7):
			print "\nchance # ",i+1,' : ',
			user_input = list(raw_input(" "))
			input_chk = self.checkInput(user_input)
			while not input_chk:
				print "\t\tplease re-enter : ",
				user_input = list(raw_input(" "))
				input_chk = self.checkInput(user_input)
			self.guess = user_input
			self.processInput()
		print  'Wrong Answer! Your chances are over, You lose!'
		print 'The right answer is : ',
		for i in self.question:
			print i,
		self.continueGame()
	

q = CowsAndBulls()


# from sys import exit
# def func(s):
# 	# flag=1
# 	t=s.split(' ')
# 	print "t= ",t
# 	for i in range(4):
# 		j=0
# 		while(j<4):
# 			if t[i]== t[j] and i!=j:
# 				# flag=0
# 				return False
# 			j=j+1
# 	return True

# def func2(st):
# 		s1=''
# 		for i in range(4):
# 			s1+=st[i]
# 			s1+=' '
# 		return s1
# #*********************

# n=range(1000,1035)
# num=[]
# ln=len(n)
# for j in range(ln):
# 	st=str(n[j])
# 	num.append(func2(st))
# print "n1 ",num
# l=len(num)
# res=[]
# j=0
# print range(l)
# for i in range(l):
# 	print "num[i]",num[i]
# 	stat=func(num[i])
# 	print "stat= ",stat
# 	if stat:
# 		print "j: ",j
# 		res.append(num[i])
# 		j+=1

# print "res=",res

#*******************************

def space(st):
	s1=''
	l=len(st)
	for i in range(l):
		s1+=st[i]
		s1+=' '
	return s1



def isrange(n):
	if isnum(n):
		nu=int(n)
		chk=True
		if(nu>9999 or nu<1000):
			chk=False
		return chk
	else:
		return False



def repeat(s):
	# s=space(n)
	t=s.split(' ')
	for i in range(4):
		j=0
		while(j<4):
			if t[i]== t[j] and i!=j:
				return False
			j=j+1
	return True

def isnum(s):
	inp=s.split(' ')
	l=len(inp)
	flag=True
	for i in range(l-1):
		flag=inp[i].isdigit()
		if not flag:
			return False
	return True

def inputcheck(n):
	s=space(n)
	if  not isnum(s):
		return False
	elif not isrange(n):
		return False
	elif not repeat(n):
		return False
	else:
		return True


s='a b c a '
n='abca '
ans=inputcheck(n)
print "ans= ",ans

rep=repeat(s)
num=isnum(s)
ran=isrange(n)
print "rep= ",rep
print "num= ",num
print "range= ",ran




#isnum('1 2 3 4 ')



# import string
# s=""
# d=0
# print "enter a number"
# n=int(raw_input("> "))
# while(n>0):
# 	r=n%10
# 	d=d*10+r
# 	n=n/10

# while(d>0):
# 	r=d%10
# 	s+=str(r)
# 	s+=" "
# 	d=d/10

# print "num is",s



# numb='1 2 3 4'
# bulls=0
# cows=0
# def check(gs):
# 	new=numb.split(' ')
# 	inp=gs.split(' ')
# 	cows=0
# 	bulls=0
# 	print "cows= ",cows
# 	print "bulls= ",bulls
# 	print "new= ",new
# 	print "inp= ",inp
# 	for i in range(4):
# 		if new[i]==inp[i]:
# 			bulls+=1
# 		if bulls==4:
# 			print "You win.."
# 			exit(1)
# 		for i in range(4):
# 			for j in range(4):
# 				if inp[i]==new[j] and i!=j:
# 					cows+=1
# 	print bulls," Bulls and ",cows," Cows"

# gs='1 2 3 4'
# for i in range(4):
# 	check(gs)
# print "you lose!.."


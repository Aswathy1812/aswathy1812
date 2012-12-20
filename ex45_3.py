# from sys import exit
import string
s=""
d=0
print "enter a number"
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

print "num is",s



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


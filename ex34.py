from string import *
animals=['bear','python','peacock','kangaroo','whale','platypus']
print "Animals= ",animals
print "The animal at 1 is a "+animals[1]
print "The 3rd animal is at 2 and is a "+animals[2]
print "The 1st animal is at 0 and is a "+animals[0]
print "The animal at 3 is a "+animals[3]
print "The 5th animal is at 4 and is a "+animals[4]
print "The animal at 2 is a "+animals[2]
print "The 6th animal is at 5 and is a "+animals[5]
print "The animal at 4 is a "+animals[4]

alphabets=[]
i=0
num=range(26)
while i<26:
	alphabets+=letters[i]
	i+=1
print "\nAlphabets\n" 
for i in num:
	print "The alphabet at ",(i+1)," is "+ alphabets[i]


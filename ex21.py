def add(a,b):
	print "ADDING..%d and %d"%(a,b)
	return a+b

def sub(a,b):
	print "SUBTRACTING..%d and %d"%(a,b)
	return a+b

def mul(a,b):
	print "MULTIPLYING..%d and %d"%(a,b)
	return a+b

def div(a,b):
	print "DIVIDING..%d and %d\n"%(a,b)
	return a+b

age=add(40,2)
height=sub(180,14)
weight=mul(10,5)
iq=div(180,2)

print "\nAge: %d\nHeight: %d\nWeight: %d\nIQ: %d"% (age,height,weight,iq)

what=add(age,sub(height,mul(weight,div(iq,2))))
print "\nThe answer is: ",what,". Correct?"
def accept_elements(n):
	numbers=[]
	numbers=range(n)
	print "The numbers:\n"
	for i in numbers:
		print i

print "Enter values for limit "
limit=raw_input()
accept_elements(int(limit))
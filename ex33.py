def accept_elements(n,k):
	i=0
	numbers=[]

	while i<n:
		numbers.append(i)
		i=i+k
		print "numbers now:",numbers

	print "The numbers: "
	for num in numbers:
		print num
print "Enter values for limit and increment"
limit=raw_input()
inc=raw_input()
accept_elements(int(limit),int(inc))
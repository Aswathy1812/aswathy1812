people = 40
cars = 20
buses = 35


if cars>people :
	print "We should take tha cars."
elif cars<people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many buses."
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people>buses:
	print "Alright,let's just take the buses."
else:
	print "Fine, let's stay home then."

if cars>buses and cars<people:
	print "Let's take the cars"
elif cars <buses and people >cars:
	print "Let's take the buses"
else:
	print "Let's walk"
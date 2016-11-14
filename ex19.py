def cheese_and_crackers(cheese_count,boxex_of_crackers):
	print "You have %d cheeses"%cheese_count
	print "You have %d boxes of crackers"% boxex_of_crackers

print "\nGiving numbers directly:\n"
cheese_and_crackers(20,30)

print "\nGiving from script:\n"
cheese=10
crackers=50
cheese_and_crackers(cheese,crackers)

print "\nMath inside:\n"
cheese_and_crackers(40+20,50+10)

print "\nCombining variables and math:\n"
cheese_and_crackers(cheese+60,crackers+30)
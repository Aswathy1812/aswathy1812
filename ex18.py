def print_two(*args):
    arg1,arg2=args

    print "\narg1: %r\narg2: %r"%(arg1,arg2)

def print_two_again(arg1,arg2):
	print "\narg1: %r\narg2: %r"%(arg1,arg2)

def print_one(arg1):
	print "\narg1: %r"% arg1

def print_none():
	print "\nThere is nothing to print.."

print_two('one','two')
print_two_again('one again','two again')
print_one('only one')
print_none()


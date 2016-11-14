from sys import argv
script, filename=argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)

def print_a_line(line_count,f):
	print line_count,f.readline()

current_file=open(filename)

print "\nPrinting the whole file.."
print_all(current_file)

print "\nRewinding.."

rewind(current_file)

print "\nPrinting line by line.."
line=1
print_a_line(line,current_file);#line_count=1

line=line+1
print_a_line(line,current_file);#line_count=2

line+=1
print_a_line(line,current_file);#line_count=3

from sys import argv
from os.path import exists
script,from_file,to_file=argv

print "\nCopying date from %s to %s"%(from_file,to_file)

print "\nDoes %s exist? %r"%(from_file,exists(from_file))
print "\nDo you want to continue?(ENTER/CTRL^C)"
raw_input()
print "Copying from file %s to file %s"%(from_file,to_file)
infile=open(from_file)
indata=infile.read()

outfile=open(to_file,'w')
outdata=outfile.write(indata);

print "\nFiles copied!\n"
infile.close()
outfile.close()
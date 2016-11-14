from sys import argv

name,filename=argv

print "Opening file %s in read mode.."%filename
        #opening the file in read mode
temp=open(filename,'r')
        #reading the contents of the file
data=temp.read()
        #printing the contents of the file
print "\nThe data in the file %s is :\n\n%s"%(filename,data)
print "Closing the file.."
        #closing the file
temp.close()

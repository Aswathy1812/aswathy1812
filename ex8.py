formatter="%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.", 
          #since the above line has a single quotes inside the string,
           #it is enclosed in double quotes in the o/p 
"So I said goodnight."
)


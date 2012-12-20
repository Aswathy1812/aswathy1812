class Animal(object):
    def __init__(self):
        self.atype= "wild or domestic"
        self.name="Animal"
    
    def disp(self):
        print self.name," is ",self.atype,"\n"

##dog is-a animal
class Dog(Animal):
    def __init__(self,atype,name):
        self.atype= atype
        self.name=name
    
    def display(self):
        print self.name," is a Dog"
        print "It is a ",self.atype," animal.\n"

##cat is-a animal
class Cat(Animal):
    def __init__(self,atype,name):
        self.atype= atype
        self.name=name
       
    def display(self):
        print self.name," is a Cat"
        print "It is a ",self.atype," animal.\n"

a1=Animal()
a1.disp()

Roger=Dog("domestic","Roger")
Roger.display()
Roger.disp()
Kitty=Cat("domestic","Kitty")
Kitty.display()
Kitty.disp()



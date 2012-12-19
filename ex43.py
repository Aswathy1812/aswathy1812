
class questions(object):
    def user_ch(self):  
        print "There are 3 boxes"
        print "Each box contains an animal"
        print "Please choose a box \n\t.a\n\t.b\n\t.c"
        self.ch=raw_input("> ")
        if self.ch=='a':
            self.hint_fish()
        if self.ch=='b':
            self.hint_dog()
        if self.ch=='c':
            self.hint_crow()

    def hint_fish(self):
        print "It lives in water..can u guess?"
        self.gs=self.guess()
        if self.gs=='fish':
            self.win=1
        else:
            self.win=0

    def hint_dog(self):
        print "It guards our houses..can u guess?"
        self.gs=self.guess()
        if self.gs=='dog':
            self.win=1
        else:
            self.win=0

    def hint_crow(self):
        print "It is a black bird..can u guess?"
        self.gs=self.guess()
        if self.gs=='crow':
            self.win=1
        else:
            self.win=0

    def guess(self):
        self.gs=raw_input("> ")
        return self.gs
    
class answers(questions):

    def res(self,ob):
        if ob.win==1:
            print "You win!"
        else:
            print "You lose!"


q=questions()
a=answers()

q.user_ch()
a.res(q)

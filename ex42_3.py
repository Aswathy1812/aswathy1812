from sys import exit
from random import randint

class game(object):
    def __init__(self):

        #self.start=start
        self.quips=[
        "You died. You are bad at this.",
        "Your mom would be proud. If she were smarter.",
        "Such a loser.",
        "I have a small puppy that's better at this."
        ]
    def death(self):
        print self.quips[randint(0, len(self.quips)-1)]
        exit(1)

class engine(game):
    def runner(self):
        p=princess()

class princess(game):
    def __init__(self):
        self.explain="""
        You see a beautiful Princess with a shiny crown.
        She offers you some cake.
        
            .eat it
            .do not eat it
            .make her eat it
        """
        super(princess,self).__init__()
        print self.explain
        self.choice=raw_input("> ")
        self.trick()
    def trick(self):
        eat_it=self.choice
        if eat_it == "eat it":
            print "You explode like a pinata full of frogs."
            print "The Princess laughs and eats the frogs. Yum!"
            self.death()

        elif eat_it == "do not eat it":
            print "She throws the cake at you and it cuts off your head."
            print "The last thing you see is her munching you. Yum!"
            self.death()

        elif eat_it == "make her eat it":
            print "The Princess screams as you cram the cake in her mouth."
            print "Then she smiles and cries and thanks you for saving her."
            print "She points to a tiny door and says, 'The Koi needs cake too.'"
            print "She gives you the very last bit of cake and shoves you in."
            g=goldkoipond()
            
        else:
            print "The princess looks at you confused and just points at the cake."
            p=princess()

class goldkoipond(game):
    def __init__(self):
        self.explain="""
        There is a garden with a koi pond in the center.
        You walk close and see a massive fin poke out.
        You peek in and a creepy looking huge Koi stares at you.
        It opens its mouth waiting for food.
        
            .feed it
            .do not feed it
            .throw it in
        """
        super(goldkoipond,self).__init__()
        print self.explain
        self.choice=raw_input("> ")
        self.trick()
    def trick(self):
        feed_it=self.choice
        if feed_it == "feed it":
            print "The Koi jumps up, and rather than eating the cake, eats your arm."
            print "You fall in and the Koi shrugs than eats you."
            print "You are then pooped out sometime later."
            self.death()

        elif feed_it == "do not feed it":
            print "The Koi grimaces, then thrashes around for a second."
            print "It rushes to the other end of the pond, braces against the wall..."
            print "then it *lunges* out of the water, up in the air and over your"
            print "entire body, cake and all."
            print "You are then pooped out a week later."
            self.death()

        elif feed_it == "throw it in":
            print "The Koi wiggles, then leaps into the air to eat the cake."
            print "You can see it's happy, it then grunts, thrashes..."
            print "and finally rolls over and poops a magic diamond into the air"
            print "at your feet."

            b=bearwithsword()
           
        else:
            print "The Koi gets annoyed and wiggles a bit."
            g=goldkoipond()

class bearwithsword(game):
    def __init__(self):
        self.explain="""
        Puzzled, you are about to pick up the fish poop diamond when
        a bear bearing a load bearing sword walks in.
        Hey! That\'s my diamond! Where\'d you get that!?
        It holds its paw out and looks at you.
        
            .give it
            .say no
        """
        super(bearwithsword,self).__init__()
        print self.explain
        self.choice=raw_input("> ")
        self.trick()
    def trick(self):
        give_it=self.choice
        if give_it == "give it":
            print "The bear swipes at your hand to grab the diamond and"
            print "rips your hand off in the process. It then looks at"
            print 'you and says, "Oh crap, sorry about that."'
            print "It tries to put your hand back on, but you collapse."
            print "The last thing you see is the bear shrug and eat you."
            self.death()

        elif give_it=="say no":
            print "The bear looks shocked. Nobody has ever told a bear"
            print "with a broadsword 'no'. It asks, "
            print '"Is it because it\'s not a katana? I could go get one!"'
            print "It then runs off and now you notice a big iron gate."
            print '"Where the hell did that come from?"You say.'

            b=bigirongate()

        else:
            print "The bear look puzzled as to why you'd do that."
            b=bearwithsword()

class bigirongate(game):
    def __init__(self):
        self.explain="""
        You walk up to the big iron gate and see there's a handle.
        
            .open it
            .knock at the door
        """
        super(bigirongate,self).__init__()
        print self.explain
        self.choice=raw_input("> ")
        self.trick()

    def trick(self):
        open_it=self.choice
        if open_it=='open it':
            print "You open it and you are free!"
            print "There are mountains. And berries! And..."
            w=winroom()
        
        if open_it=='knock at the door':
            print "Oh,but then the bear comes with his katana and stabs you."
            print '"Who\'s laughing now!? Love this katana."'
            self.death()

        else:
            print "That doesn't seem sensible. I mean, the door's right there."
            b=bigirongate()

class winroom(game):
    def __init__(self):
        self.explain="""
        And finally, YOU WIN!
        *********************
        """
        print self.explain
        exit(1)

g=game()
e=engine()
e.runner()
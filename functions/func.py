def repeat(s):
	t=s.split(' ')
	l=len(t)
	for i in range(l):
		j=0
		while(j<l):
			if t[i]== t[j] and i!=j:
				return False
			j=j+1
	return True

def space(st):
	s1=''
	l=len(st)
	for i in range(l):
		s1+=st[i]
		s1+=' '
	return s1

def isnum(s):
	inp=s.split(' ')
	l=len(inp)
	flag=True
	for i in range(l-1):
		flag=inp[i].isdigit()
		if not flag:
			return False
	return True

def isrange(n):

	nu=int(n)
	chk=True
	if(nu>9999 or nu<1000):
		chk=False
	return chk

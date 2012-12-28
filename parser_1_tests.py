from nose.tools import *
from ex49_1 import parser_1

def test_peek():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.peek(c1)
    assert_equal(res,'noun')
    res=parser_1.ip.peek(c2)
    assert_equal(res,'verb')
    res=parser_1.ip.peek(c3)
    assert_equal(res,'stop')
 
def test_skip():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.skip(c3,'stop')
    assert_equal(res,None)
    res=parser_1.ip.skip(c1,'noun')
    assert_equal(res,None)
    res=parser_1.ip.skip(c2,'verb')
    assert_equal(res,None)
    
def test_match():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.match(c3,'stop')
    assert_equal(res,('stop','s'))
    res=parser_1.ip.match(c2,'verb')
    assert_equal(res,('verb','v'))
    res=parser_1.ip.match(c1,'noun')
    assert_equal(res,('noun','n'))

def test_verb():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    c4=[('direction','d')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.parse_verb(c2)
    assert_equal(res,('verb','v'))
    assert_raises(Exception,parser_1.ip.parse_verb,c1)
    assert_raises(Exception,parser_1.ip.parse_verb,c3)
    assert_raises(Exception,parser_1.ip.parse_verb,c4)
    
def test_object():
    c1=[('noun','n')]
    c2=[('direction','d')]
    c3=[('stop','s')]
    c4=[('verb','v')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.parse_object(c1)
    assert_equal(res,('noun','n'))
    res=parser_1.ip.parse_object(c2)
    assert_equal(res,('direction','d'))
    assert_raises(Exception,parser_1.ip.parse_object,c3)
    assert_raises(Exception,parser_1.ip.parse_object,c4)
   
def test_subject():
    c1=[('noun','princess')]
    c2=[('verb','kill'),('stop','the'),('noun','bear')]
    ip=parser_1.InputSentence()
    subj=parser_1.ip.match(c1,'noun')
    res=parser_1.ip.parse_subject(c2,subj)
    assert_equal(res.subject,'princess')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')

def test_sentences():
    c3=[('error',' ')]#('verb','kill'),('stop','the'),('noun','bear')]
    c1=[('direction','d'),('verb','kill'),('stop','the'),('noun','bear')]
    c2=[('noun','princess'),('verb','kill'),('stop','the'),('noun','bear')]
    c4=[('verb','kill'),('stop','the'),('noun','bear')]
    ip=parser_1.InputSentence()
    res=parser_1.ip.parse_sentence(c2)
    assert_equal(res.subject,'princess')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')
    res=parser_1.ip.parse_sentence(c4)
    assert_equal(res.subject,'player')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')
    assert_raises(Exception,parser_1.ip.parse_sentence,c3)
    assert_raises(Exception,parser_1.ip.parse_sentence,c1)




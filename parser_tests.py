from nose.tools import *
from ex49 import parser

def test_peek():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    res=parser.peek(c1)
    assert_equal(res,'noun')
    res=parser.peek(c2)
    assert_equal(res,'verb')
    res=parser.peek(c3)
    assert_equal(res,'stop')
 
def test_skip():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    res=parser.skip(c3,'stop')
    assert_equal(res,None)
    res=parser.skip(c1,'noun')
    assert_equal(res,None)
    res=parser.skip(c2,'verb')
    assert_equal(res,None)
    
def test_match():
    c1=[('noun','n')]
    c2=[('verb','v')]
    c3=[('stop','s')]
    res=parser.match(c3,'stop')
    assert_equal(res,('stop','s'))
    res=parser.match(c2,'verb')
    assert_equal(res,('verb','v'))
    res=parser.match(c1,'noun')
    assert_equal(res,('noun','n'))

def test_verb():
    c1=[('noun','n')]
        c2=[('verb','v')]
        c3=[('stop','s')]
    c4=[('direction','d')]
        res=parser.parse_verb(c2)
    assert_equal(res,('verb','v'))
    assert_raises(Exception,parser.parse_verb,c1)
    assert_raises(Exception,parser.parse_verb,c3)
    assert_raises(Exception,parser.parse_verb,c4)
    
def test_object():
    c1=[('noun','n')]
    c2=[('direction','d')]
    c3=[('stop','s')]
    c4=[('verb','v')]
    res=parser.parse_object(c1)
    assert_equal(res,('noun','n'))
    res=parser.parse_object(c2)
    assert_equal(res,('direction','d'))
    assert_raises(Exception,parser.parse_object,c3)
        assert_raises(Exception,parser.parse_object,c4)
   
def test_subject():
    c1=[('noun','princess')]
    c2=[('verb','kill'),('stop','the'),('noun','bear')]
    subj=parser.match(c1,'noun')
    res=parser.parse_subject(c2,subj)
    assert_equal(res.subject,'princess')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')

def test_sentences():
    c3=[('error','v'),('verb','kill'),('stop','the'),('noun','bear')]
    c1=[('direction','d'),('verb','kill'),('stop','the'),('noun','bear')]
    c2=[('noun','princess'),('verb','kill'),('stop','the'),('noun','bear')]
    c4=[('verb','kill'),('stop','the'),('noun','bear')]
    res=parser.parse_sentence(c2)
    assert_equal(res.subject,'princess')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')
    res=parser.parse_sentence(c4)
    assert_equal(res.subject,'player')
    assert_equal(res.verb,'kill')
    assert_equal(res.object,'bear')
    assert_raises(Exception,parser.parse_sentence,c3)
    assert_raises(Exception,parser.parse_sentence,c1)





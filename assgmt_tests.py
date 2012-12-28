from nose.tools import *
from ex50 import assgmt

def main_trick_test():
	pass
def river_trick_test():
	r=assgmt.River()
	vb=['walk','go','move','climb','run']
	ob=['swan','bridge']
	for i in range(3):
		res=assgmt.r.trick(vb[i],ob[0])
		assert_equal(res,'swan')
	for i in range(5):
		res=assgmt.r.trick(vb[i],ob[1])
		assert_equal(res,'bridge')

def farm_trick_test():
	pass

def pond_trick_test():
	pass

def cattle_trick_test():
	pass
def swan_trick_test():
	pass
def bridge_trick_test():
	pass


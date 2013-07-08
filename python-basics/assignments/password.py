#!/usr/bin/env python

# NOTE: these pieces from the standard library will help you
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from random import randint, choice, shuffle

# NOTE: examples of use
# ascii_lowercase, ascii_uppercase, digits, punctuation are 
#   lists of ASCII characters
assert 'a' in ascii_lowercase and len(ascii_lowercase) == 26
assert 'A' in ascii_uppercase and len(ascii_uppercase) == 26
assert '1' in digits          and len(digits) == 10
assert '!' in punctuation     and len(punctuation) == 32
# randint gives a random number between [a,b] (i.e., inclusive of a and b)
assert randint(1,10) in (1,2,3,4,5,6,7,8,9,10)
# choice gives you a random element from a list or tuple
assert choice(digits) in '123456789'
assert choice(ascii_lowercase) in 'abcdefghijklmnopqrstuvwxyz'

# TODO: write me!
def new_password():
	''' gives a new password that satisfies the requirements
	
	requirements:
	1. must be random
	2. must be 8-characters long
	3. must have at least one digit, at least one punctuation, at least one
	   lowercase, AND at least one uppercase letter
	'''
	pass

# TODO: it might be helpful to write this, too
def valid_password(password):
	''' determines if a password meets the requirements

	requirements:
	(1. must be random -- too difficult to check here)
	2. must be 8-characters long
	3. must have at least one digit, at least one punctuation, at least one
	   lowercase, AND at least one uppercase letter
	'''
	return True

# NOTE: this is an encoded solution
#       the programme will decode it automatically
#         so you can check your results against it yourself
#       it will create a function called `solution' and a 
#          function called `validate'
solution = None
validate = None
exec '''
qrs fbyhgvba():
	nyy_punenpgref = nfpvv_ybjrepnfr + nfpvv_hccrepnfr + qvtvgf + chapghngvba
	cnffjbeq = [pubvpr(nfpvv_ybjrepnfr), pubvpr(nfpvv_hccrepnfr),
	            pubvpr(qvtvgf), pubvpr(chapghngvba)] + \
	           [pubvpr(nyy_punenpgref) sbe _ va kenatr(4)]
	fuhssyr(cnffjbeq)
	erghea ''.wbva(cnffjbeq)
qrs inyvqngr(cnffjbeq):
	erghea yra(cnffjbeq) == 8                   naq \
	       frg(cnffjbeq) & frg(nfpvv_ybjrepnfr) naq \
	       frg(cnffjbeq) & frg(nfpvv_hccrepnfr) naq \
	       frg(cnffjbeq) & frg(qvtvgf)          naq \
	       frg(cnffjbeq) & frg(chapghngvba)
'''.decode('rot13') in locals(), globals()

if __name__ == '__main__':
	# NOTE: some simple tests
	assert not valid_password('xyz')      and not validate('xyz') # too short!
	assert not valid_password('p@ssw0rd') and not validate('p@ssw0rd') # no uppercase 
	assert not valid_password('P@ssword') and not validate('P@assword') # no digits 
	assert valid_password('P@ssw0rd')     and validate('P@ssw0rd')	

	# generate 100 passwords and check for duplicates
	user_passwords = set()
	soln_passwords = set()
	for _ in xrange(100):
		user_password = new_password()
		soln_password = solution()
		assert valid_password(user_password) and validate(user_password)
		assert valid_password(soln_password) and validate(soln_password)
		assert user_password not in user_passwords
		assert soln_password not in soln_passwords
		user_passwords.add(user_password)
		soln_passwords.add(soln_password)

	print 'All the tests passed! Great job!'

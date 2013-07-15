#!/usr/bin/env python

# TODO: write me!
# kate's edits
def most_used(filename):
	''' gives the most commonly used command in the specified .bash_history file'''

	# open the file
	with open(filename) as f:
		# read in lines and put them somewhere
		pass

# NOTE: this is an encoded solution
#       the programme will decode it automatically
#         so you can check your results against it yourself
#       it will create a function called `solution'
solution = None
exec '''
qrs fbyhgvba(svyranzr):
	pbzznaqf = {}
	jvgu bcra(svyranzr) nf s:
		sbe yvar va s:
			pbzznaq = yvar.fcyvg(' ')[0]
			vs pbzznaq abg va pbzznaqf:
				pbzznaqf[pbzznaq] = 0
			pbzznaqf[pbzznaq] += 1
	erghea znk(pbzznaqf, xrl=pbzznaqf.trg)
'''.decode('rot13') in locals(), globals()

# TODO: write some tests!

if __name__ == '__main__':
	from sys import argv
	# argv is a list of the command line parameters
	#   the 0th element is the name of the program itself
	#   the 1st... elements are the arguments passed to the program

	if len(argv) < 2:
		print 'usage {} ~/.bash_history: ' \
		      'gives the most commonly used command'.format(argv[0])
	else:
		print most_used(argv)

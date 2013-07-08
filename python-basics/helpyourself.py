#!/usr/bin/env python

# PURPOSE
# #######

# this tutorial shows you two common tools you can use when programming
#   to help yourself: dir, type, help

# note that the official Python 2 documentation is available at
#   http://docs.python.org/2/

# help()
# ######

# when using Python interactively, you can view help
#   for a function by typing:

help(len)

# this will give you the help text for that function
#    which should include inputs, outputs, and arguments

# when you write your own function or class, be sure to add a `docstring'
#   so that you can provide the same help to others

# the docstring is a string that appears on the first line of the 
#   definition
# conventions for writing these are in PEP-256
#   http://www.python.org/dev/peps/pep-0257/

# in general, the first line should give a brief description of what
#   the function does, then there should be a blank line,
#   then next block of text should give a detailed description

# e.g.,

def fibonacci(n):
	'''prints the fibonacci numbers not exceeding n
	
	e.g., fibonacci(10) prints 1, 1, 2, 3, 5, 8	'''
	a, b = 1, 1
	while a < n:
		print a
		a, b = b, a+b

# type()
# ######

# type() has a lot of uses, but one simple use when working interactively
#   is to query an object to determine what type it is
# this can help if you need to debug a function that was expecting
#   a string but receiving a list

x = [1,2,3]
print type(x)

x = 'one two three' 
print type(x)

# for rich types or systems with large object heirarchies,
#   this can be helpful to find the code that runs when a certain method
#   is called

# dir()
# #####

# dir() should only be used interactives

# it's named similarly to the `dir` command in MS-DOS, but it lists
#   the methods that you can call on an object or the contents of a module

# so, for example, if you forgot the name of the random function you wanted
#   from the random module, you could type

import random
dir(random)

# you should see a list of all the functions in random. 

# similarly, if you forgot if uppercasing a string was 'asdf'.uppercase()
#   or 'asdf'.upper() you could type

x = 'asdf'
dir(x)

#!/usr/bin/env python

from __future__ import division
from __future__ import unicode_literals

# PURPOSE
# #######

# this tutorial details the use of `expressions' and variables in Python
# in Python, an expression is a string of code that returns a value

# this tutorial covers:
#   variable assignment and use
#   arithmetic expressions
#   logical expressions
#   bitwise expressions
#   comparison expressions
#   True/False expressions
#   string expressions
#   indexing expressions
#   calling functions & methods

# VARIABLE ASSIGNMENT AND USE
# ###########################

# in Python, we declare and initialize a variable in the same line
#   with the following simple syntax

city = 'new york'
population = 8245000
print city, 'has a population of', population

# if we want to be terse, we can do this all on one line

city, population = 'newark', 277540
print city, 'has a population of', population

# one Python idiom is to use this to swap two variables!
city1 = 'new york'
city2 = 'newark'

city1, city2 = city2, city1
assert city1 == 'newark' and city2 == 'new york'

# variables in Python are not like variables in math;
#   they are merely names that reference a certain value
# as a result, they can be re-assigned and mutated

manhattan = 1619090
bronx = 1408473
brooklyn = 2565635
queens = 2272771
staten_island = 470728

total_population = 'who knows?'

total_population = 0 # reassign it
 
total_population = manhattan # reassign it
total_population = total_population + bronx
total_population = total_population + brooklyn
total_population = total_population + queens
total_population = total_population + staten_island

assert total_population == 8336697 == \
       manhattan + bronx + brooklyn + queens + staten_island

# ARITHMETIC OPERATORS
# ####################

# Python supports basic arithmetic operators for numbers: +, -, *, /, **, //, %

assert 1 + 2 == 3
assert 4 - 2 == 2
assert 2 * 3 == 6
assert 5 / 2 == 2.5

# // means "truncating division" which means dividing and throwing away
#   the fractional part
# this is the division behavior you see for integers in languages like C, C++,
#   and Java

assert 5 // 2 == 2

# % means "modulo" like in C, C++, and Java.
# it gives the remainder of a division and can be used to check
#   for divisibility

assert 23 % 5 == 3
assert 4 % 2 == 0 # divides evenly

# note that Python has a full "numeric tower" so there is no 
#   overflow like in C, C++, Java

x = 9223372036854775807
assert x == 2 ** (64-1) - 1 # maximum int in 64-bits

y = x + 1
assert y > x # no overflow!

# there are +=, -=, *=, /=, **=, //=, %= variants for each
#   of these operators to perform the "augmented" assignment: e.g.,
#     x = x + ...
#     x = x - ...

x = 10
x *= 3
assert x == 30

# LOGICAL OPERATORS
# #################

# Python also has the logical operators and, or, not

x = True
assert x

x = True and False
assert not x

x = True or False
assert x

# in Python, we have strict True and False symbols

assert True
assert not False

# these are of the bool type

assert type(True) is bool
assert type(False) is bool

# however, we often deal with things that are True-equivalent or
#   False-equivalent

# False-equivalent things are what you might expect them to be:
#   False, 0, 0.0, empty strings (''), empty lists ([])
assert not False
assert not 0
assert not 0.0
assert not ''
assert not []
assert not ()
assert not {}

# True-equivalent things are everything else
assert True
assert 1
assert 1.0
assert 'abc'
assert ['a', 'b', 'c']
assert ('a', 'b', 'c')
assert {'one': 1, 'two': 2}

# in general, objects are considered True-equivalent by default,
#   but this behavior can be customized. Adding certain behaviour
#   to an object can also affect what states are considered
#   True-equivalent or False-equivalent
class Foo(object): pass
foo = Foo()
assert foo # considered True by default

# BITWISE EXPRESSIONS
# ###################

# you'll probably rarely use bitwise expressions in Python, but 
#   the language does provide &, |, and ^ for bitwise-and, bitwise-or,
#   and bitwise-xor

assert 64 & 1 == 0
assert 68 | 5 == 69
assert 68 ^ 5 == 65

# COMPARISON EXPRESSIONS
# ######################

# there are also rich comparison operators in Python:
#   ==, !=, <>, <, <=, >, >=, in, is
#   for equal, not equal (!= and <>), less than (or equal to,)
#   greater than (or equal to,) contains, and identicality

x = 10
assert x == 10
assert x != 20
assert x <> 20 # <> is very rarely seen in practice
assert x > 4
assert x >= 4 and x >= 10
assert x < 15
assert x <= 15 and x <= 10

# `in` can be used to determine if an element belongs to 
#    some collection

assert x in (1, 10, 1000, 10000)
assert x not in (1, 2, 4, 8, 16, 32)

# note that these operators can be chained
assert 1 < x < 100

# the `is` operator indicates that two objects are identical
#   by identity. This is rarely used outside of the idiom

x = None
assert x == None and x is None

# it may appear to work for integers and certain strings,
#   but this is an implementation detail that should not
#   be relied upon ("interning")

# STRINGS
# #######

# strings can be defined in Python with single, double, or tripled
#   quotes
# each of these forms are equivalent (unlike in bash) and are
#   provided for convenience
# the triple single and triple double quotes let you write
#   multiline strings

city = 'new york'
print 'I live in the city of', city

city = "new york"
print "I live in the city of", city

city = '''
houston
new york
'''
print "I've lived in the cities of", city

# note that string literals that are placed side by side
#   are automatically and implicitly concatenated

# TERNARY CONDITIONAL
# ###################

# the other operators we have looked at have been binary
#   (they take two arguments) or unary (they take one argument, e.g., not)
#   but Python also provides a ternary conditional operator
#   like ?: in C and C++

x = 20
x = 'new york' if x > 10 else 'newark'
assert x == 'new york'

# ARRAY INDEXING AND SLICING
# ##########################

# Python arrays can be indexed and sliced in very rich ways

x = ['manhattan', 'brooklyn', 'bronx', 'queens', 'staten island'] 

assert len(x) == 5

# get the nth element, counting from 0
assert x[0] == 'manhattan'
assert x[1] == 'brooklyn'
assert x[4] == 'staten island'

# get the nth from the end element, counting from -1
assert x[-1] == 'staten island'
assert x[-2] == 'queens'
assert x[-5] == 'manhattan'

# we can also "slice" into the array with the syntax
#   x[start:stop:step]
# the start is the element where we start (counting from 0)
# the stop is the element where we stop (non-inclusive, defaulting to the last)
# the step is the stepping of elements (defaulting to every 1 element)
assert x[1:3] == ['brooklyn', 'bronx']
assert x[1::2] == ['brooklyn', 'queens']

# an idiom you may run across is [::-1] to get the elements
#   from the beginning, to the end, going by -1 (backwards)
# this gives a reversed version of the list!

assert x[::-1] == ['staten island', 'queens', 'bronx', 'brooklyn', 'manhattan']

# CALLING FUNCTIONS AND METHODS
# #############################

# functions can be called and their results can be assigned to variables

x = ['manhattan', 'brooklyn', 'bronx', 'queens', 'staten island'] 
size_x = len(x)

assert size_x == len(x) == 5

# functions with more than one parameter can take
#    "positional arguments" and "keyword arguments"

# one common example of a keyword argument is the keyfunc
#   parameter that many built-in functions use
from operator import neg # negates a number
assert neg(10) == -10

assert max([1,2,4,8]) == 8
assert max([1,2,4,8], key=neg) == 1

# Python objects also have "methods" which are called with the syntax
#   x.y()

# string objects have a method called .upper() which returns an uppercased
#   version
x = 'new york'
assert x.title() == 'New York'
assert x.upper() == 'NEW YORK'
assert x.lower() == 'new york'

# these can be chained
assert x.encode('rot13') == 'arj lbex'
assert x.encode('rot13').upper() == 'ARJ LBEX'

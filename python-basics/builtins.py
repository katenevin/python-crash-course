#!/usr/bin/env python

# PURPOSE
# #######

# this file is a brief introduction to some of the more
#   useful builtin functions

# a builtin function is a function that is provided
#   without having to import anything

# note that these are merely provided by default, and they can be overridden

# this tutorial will look at:

any
all
min
max
sum
zip
sorted
reversed
enumerate
xrange
open
map
filter
reduce

# any, all
# ########

# any returns True if any of the arguments in the provided Iterable
#   are True

assert any([True, False, 0.0, 0])

# all returns True if all of the arguments in the provided Iterable
#   are True

assert not all([True, False, 0.0, 0])
assert all([True, 1, 'asdf'])

# they might look something like:
def any(iterable):
	for element in iterable:
		if element:
			return True
	return False

def all(iterable):
	for element in iterable:
		if not element:
			return False
	return True

# min, max
# ########

# min gives the minimum value of the provided Iterable, using the 
#   provided keyfunction to determine the comparison
# max does the opposite

assert min([1,2,4,8,16]) == 1
assert max([1,2,4,8,16]) == 16

from operator import neg
assert min([1,2,4,8,16], key=neg) == 16
assert max([1,2,4,8,16], key=neg) == 1

# they might look something like:
def min(iterable, key=lambda x: x):
	min_element = next(iterable)
	for element in iterable:
		k = key(element)
		if k < min_element:
			min_element = k
	return min_element

def max(iterable, key=lambda x: x):
	max_element = next(iterable)
	for element in iterable:
		k = key(element)
		if k > max_element:
			max_element = k
	return max_element

# sum
# ###

# sum gives you the sum of an Iterable

assert sum([1,2,3,4]) == 1+2+3+4 == 10
assert sum([[1,2], [3,4]], []) == [] + [1,2] + [3,4] == [1,2,3,4]

# it might look something like:
def sum(iterable, start=None):
	total = next(iterable) if start is None else start 
	for element in iterable:
		total += element
	return total

# zip
# ###

# zip takes two iterables and combines them like a zipper

assert zip([1,2,3], 'abc') == [(1, 'a'), (2, 'b'), (3, 'c')]
assert zip('abc', 'defg')  == [('a', 'd'), ('b', 'e'), ('c', 'f')]

# it might look something like:
def zip(*iterables):
	result = []
	while True:
		element = ()
		for iterable in iterables:
			try:
				element += next(iterable)
			except StopIteration:
				return result
		result.append(element)

# sorted
# ######

# sorted returns a stably sorted version of an iterable

assert sorted([2,5,1,4,6,1]) == [1,1,2,4,5,6]

# it uses an efficient, hybrid sort (Timsort)

# reversed
# ########

# reversed returns a reversed version of an iterable

assert list(reversed([1,2,4,8,16])) == [16,8,4,2,1]

# it might look something like:
def reversed(iterable):
	iterable = list(iterable)
	iterable.reverse()
	return iter(iterable)

# enumerate
# #########

# enumerate is like zipping a counting sequence
#   with your iterable

# it is the preferred way to iterate through a sequence
#   while knowing with number element you are on

assert list(enumerate('abc')) == [(0, 'a'), (1, 'b'), (2, 'c')]
assert list(enumerate('abc', start=30)) == \
       [(30, 'a'), (31, 'b'), (32, 'c')]

# it might look something like:
def enumerate(iterable, start=0):
	for element in iterable:
		yield start, element
		start += 1

# xrange and range
# ################

# xrange gives an iterable of numbers starting from 
#   some point, ending at some point, and stepping by some amount

# range is the same as xrange, except it gives the materialized
#   sequence instead of just a lazy iterable

# end point is NOT included
assert range(10)    == list(xrange(10))    == [0,1,2,3,4,5,6,7,8,9]
assert range(1,5)   == list(xrange(1,5))   == [1,2,3,4]
assert range(1,6,2) == list(xrange(1,6,2)) == [1,3,5]

# open
# ####

# open allows you to interact with files by reading and writing
#   to them. (It's also a context manager for convenience.

from sys import argv
# open this file
with open(argv[0]) as f:
	for lineno, line in enumerate(f):
		if 'magic string' in line:
			print lineno # should be about 189, the above line
			
# map, filter, reduce
# ###################

# map takes an iterable and a function and applies
#   that function to each element, returning a list
#   of the results

def double(x):
	return x*2

assert map(double, [1,2,4,8,16]) == [2,4,8,16,32]

# it might look something like:
def map(func, iterable):
	result = []
	for element in iterable:
		result.append(func(element))
	return result

# filter takes an iterable and a predicate function and returns a 
#   list of elements from that iterable if the predicate
#   function returns True for that element

def odd(x):
	return x % 2 == 1

assert filter(odd, [1,2,3,4,5,6]) == [1,3,5]

# it might look something like:
def filter(predicate, iterable):
	result = []
	for element in iterable:
		if predicate(element):
			result.append(element)
	return result

# reduce takes an iterable and a function and returns the
#   result of that function applied to every element of that
#   iterable
# the function takes two arguments: an accumulator and the current
#   value

from operator import mul
assert reduce(mul, [1,2,3,4,5]) == ((((1*2)*3)*4)*5) == 120

# it might look something like:
def reduce(func, iterable, start=None):
	result = next(iterable) if start is None else start
	for element in iterable:
		result = func(result, element)
	return result

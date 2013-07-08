#!/usr/bin/env python

# PURPOSE
# #######

# this tutorial briefly shows how names and bindings work
#   in Python.

# in Python, a variable definition is actually just a binding
#   of some value to a name

# values can be mutable (they can change in place) or immutable
#   (they cannot change in place)

# names, however, can always be rebound

x = [1,2,3] # lists are mutable
y = x
x += [4] # mutate the list

assert x == y == [1,2,3,4] # both x and y change

x = 'abc' # strings are immutable
y = x
x += 'd'

assert x == 'abcd' != y # x got reassigned to a new string, 'abcd'

# names are introduced into scope by assignment statements, def statements,
#   class statements, or import statements

# this introduces the name `double' into scope
def double(x):
	return x*2

assert double(10) == 20

# we can remove a binding with the `del` statement
del double

# or, we can rebind it
def double(x):
	return x + x

assert double('a') == 'aa'

del double

# if double operated on a parameter, then we must know if the
#   parameter is mutable or immutable to know whether any side effects
#   are seen

def double(x):
	x += x
	return x

x = 'a'
double(x)
assert x == 'a' # no change, since strings are immutable

x = ['a']
double(x)
assert x == ['a', 'a'] # change, since lists are mutable

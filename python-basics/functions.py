from __future__ import division

import random
import string

# basic syntax
##############

# the simplest function takes no arguments and does nothing.
# in this case, the return value is `None'.
def noop():
    pass

assert noop() is None

# we can return a value using the `return' statement.
def return_foo():
    return 'foo'

assert return_foo() == 'foo'

# functions become more useful when you accept inputs.
def return_something(something):
    return something

assert return_something(42) == 42
assert return_something('hello') == 'hello'
assert return_something('hello') != 'goodbye'

# you can take multiple arguments by separating them with commas.
def add(val1, val2):
    return val1 + val2

assert add(10, 20) == 30
assert add(10, 20) != 40

# a function can take an arbitrary number of arguments with the *args convention.
def average(*args):
    return sum(args) / len(args)

assert average(1, 2, 3) == 2
assert average(2, 4, 8) == 14 / 3

# keyword arguments take defaults:
# these arguments are positional and keyword
def add_default_five(two=2, three=3):
    return two + three

assert add_default_five() == 5
assert add_default_five(3) == 6
assert add_default_five(three=2) == 4

# you can combine these.
def add_one_by_default(val1, val2=1):
    return val1 + val2

assert add_one_by_default(4) == 5
assert add_one_by_default(5, 5) == 10
assert add_one_by_default(5, val2=10) == 15

# keyword arguments can also be done with the **kwargs syntax.
def name_my_pets(**kwargs):
    return ', '.join(['{} : {}'.format(k, v) for k, v in sorted(kwargs.items(), key=lambda x: x[0])])

assert name_my_pets(dog='fido') == 'dog : fido'
assert name_my_pets(cat='Bill Murray', fish='Ellen DeGeneres') == 'cat : Bill Murray, fish : Ellen DeGeneres'

# you can also return more than one value.
def min_max(items):
    """ Docstrings like this give us information about the program.
    min_max returns a two-tuple and takes an iterable of comparable items."""
    return min(items), max(items)

assert min_max([2, 4, 6]) == (2, 6)
assert min_max('abcd') == ('a', 'd')

# lambdas are anonymous functions. They're great for one liners, but you can't do certain things in one line.
five_random_items = lambda x: [random.choice(x) for i in range(5)]

assert len(five_random_items(range(100))) == 5
for i in five_random_items(string.ascii_letters):
    assert i in string.ascii_letters


# be careful what you pass as a default argument. Mutable types won't always do what you want.
def bad_append_one(input_list=[]):
    input_list.append(1)
    return input_list

assert bad_append_one() == [1]
assert bad_append_one() != [1]

# you probably meant to do this instead:
def append_one(input_list=None):
    if input_list is None:
        input_list = []
    input_list.append(1)
    return input_list

assert append_one() == [1]
assert append_one() == [1]

# re: a module for working with regular expressions
import re

# match a string to a regular expression
assert re.match('^he.+', 'hello, world')
assert not re.match('^he.+', 'fellow squirrels')

# leet it up.
input_string = 'we\'re the coolest kids around'
input_string = re.sub('e', '3', input_string)
input_string = re.sub('l', '1', input_string)
input_string = re.sub('t', '7', input_string)
assert input_string == 'w3\'r3 7h3 coo13s7 kids around'

# string: a bunch of things you probably would have typed out yourself otherwise
import string

assert string.digits == '0123456789'
assert string.ascii_lowercase == string.ascii_uppercase.lower()
assert string.ascii_lowercase in string.ascii_letters

# random: when predictable just won't do.
import random

# shuffle a list
assert random.shuffle([1, 2, 3, 4, 5]) != [1, 2, 3, 4, 5]

# get a random item from a list
assert random.choice([1, 2, 3, 4, 5]) in [1, 2, 3, 4, 5]
assert random.choice('python') in 'python'

# get a random number between 0 and 1
assert 0 <= random.random() < 1

# datetime: working with dates, times, and everything between
from datetime import date, datetime, timedelta

now = datetime.now()
today = date.today()
tomorrow = today + timedelta(days=1)

# dates don't include time information. If you discard time information from a datetime,
#   you should have the same information as the date.
assert now.date() == today

# a timedelta can be used to add and subtract time from dates and datetimes. These objects
#   are returned when using addition and subtraction.
assert isinstance(tomorrow - today, timedelta)
assert tomorrow - today == timedelta(days=1)
assert (now + timedelta(days=1)).date() == tomorrow

# time: related to datetime, but more unixy (plus some other stuff)
import time

# get the processor time
time.clock()

# sleep for two seconds
before = time.time()
time.sleep(2)
after = time.time()
assert after >= before + 2

# copy: for when you need a copy of an object rather than the original
import copy

# this type of assignment is pass by reference, not value.
mylist = [1, 2, 3]
mycopy = mylist

assert mylist == mycopy
assert mylist is mycopy

mycopy.append(4)
assert mylist == mycopy

# you might want this instead
mylist = [1, 2, 3]
mycopy = copy.copy(mylist)

assert mylist == mycopy
assert mylist is not mycopy

mycopy.append(4)
assert mylist != mycopy

# copy.deepcopy can be expensive, but it's necessary to find nested objects
my_inner_dict = {'1' : 1}
mydict = {'inner' : my_inner_dict}
mydict_copy = copy.copy(mydict)
mydict_deepcopy = copy.deepcopy(mydict)

assert mydict is not mydict_copy
assert mydict['inner'] is mydict_copy['inner']
assert mydict['inner'] is not mydict_deepcopy['inner']

# json: convert between python natvies and the json serialization format
import json

json_string = '{"a": 1, "b": 2, "c": 3}'
json_dict = {'a' : 1, 'b' : 2, 'c' : 3}

assert json_dict == json.loads(json_string)
assert json.dumps(json_dict, sort_keys=True) == json_string

# collections: specialty container types for data that make your life easier
import collections

# a dict subclass with a default fallback (this would not work as written with
#   a regular dictionary
ddict = collections.defaultdict(int)
for i in 'hello':
    ddict[i] += 1
assert ddict == {'h' : 1, 'e' : 1, 'l' : 2, 'o' : 1}

# objects with the  __call__ method are Callables
assert isinstance(lambda x: x, collections.Callable)
assert isinstance(object, collections.Callable)
assert not isinstance(1, collections.Callable)

# decimals provide real decimal numbers where floats don't work
from decimal import Decimal
assert .1 + .2 != .3
assert Decimal('.1') + Decimal('.2') == Decimal('.3')

# logging: for all your logging needs
import logging

# some generic logging statement
logging.info('in the logs')

# something bad happened
logging.error('please fix me')

# information about your exceptions including a traceback
try:
    1 / 0
except:
    logging.exception('Not very good at division')

# sys: information about your system
import sys

# make sure you haven't changed your recursion limit
assert sys.getrecursionlimit() == 1000

# hopefully, you're on one of these versions
assert sys.version_info.major in [2, 3]

# os: a bunch of information about your os
import os

os.name
os.system('ls')

os.path.dirname(__file__)

# hashlib: for some of your hashing needs
import hashlib

assert hashlib.md5('python').hexdigest() == '23eeeb4347bdd26bfc6b7ee9a3b755dd'
assert hashlib.md5('python').block_size == 64

# itertools: for dealing with anything iterable
import itertools

# combining iterables
assert list(itertools.chain([1, 2, 3], range(4, 11), (11, 12, 13))) == list(range(1, 14))

# finding permutations
assert list(itertools.permutations('abc', 2)) == [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]

# TODO: add the following: pprint, functools, argparse, getpass

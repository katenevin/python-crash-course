#!/usr/bin/env python

# PURPOSE
# #######

# this tutorial is a brief overview of the datatypes
#   in Python

# it covers:
list
dict
tuple
set
str
int
long
float
bool
True, False
None

# list
# ####

# lists are the basic Python container type

# they are not required to be homogenous (all elements share the same
#   type) but this is usually how they are used

# lists are mutable and ordered

# a simple list of city names
cities = ['new york', 'houston', 'los angeles']
assert len(cities) == 3
assert cities[0] == 'new york'

# add an element to the end
cities.append('chicago')
assert len(cities) == 4
assert cities[3] == cities[-1] == 'chicago'

# assign to an element
cities[3] = 'austin'

# remove an element from the end
assert cities.pop() == 'austin'

# lists can be added
borroughs = ['brooklyn', 'queens', 'bronx', 'manhattan', 'staten island']
assert ['brooklyn', 'queens'] + ['bronx', 'manhattan', 'staten island'] == \
       borroughs

# another way to do it:
borroughs = []
borroughs.extend(['brooklyn', 'queens'])
borroughs.extend(['manhattan', 'bronx', 'staten island'])
assert len(borroughs) == 5

# determine if an element belongs to a list with `in`
assert 'brooklyn' in borroughs

# sort a list
borroughs = ['brooklyn', 'queens', 'bronx', 'manhattan', 'staten island']
borroughs.sort()
assert borroughs == ['bronx', 'brooklyn', 'manhattan', 'queens', 
                     'staten island']

# reverse a list
borroughs.reverse()
assert borroughs == ['staten island', 'queens', 'manhattan', 'brooklyn', 
                     'bronx'] 

# dict
# ####

# dicts are the basic mapping type in Python. They're used all over the place
#   and the implementation is very efficient.

# a mapping is a key->value pair which supports lookup key. Mappings are 
#   called hashes or associative arrays in other languages. A key
#   may appear only once, but a value may appear multiple times.

# a mapping of city -> population
borroughs = {'manhattan': 1619090, 'bronx': 1408473, 'brooklyn': 2565635, 
             'queens': 2272771, 'staten_island': 470728}

numbers = dict(one=1, uno=1, two=2, dos=2, three=3, tres=3)

# you can test for membership with `in`
assert 'manhattan' in borroughs
assert 'jersey' not in borroughs

# you can get an item by its key using [] or .get
assert borroughs['manhattan'] == 1619090
assert borroughs.get('manhattan') == 1619090

# the difference is that if the key does not exist, .get can return a default
#   value
assert 'jersey' not in borroughs
assert borroughs.get('jersey', 100) == 100

# you can get the keys as a list with .keys, the values as a list with .values
#   and (key, value) tuples with .items

# note that dicts are UNSORTED
assert 'manhattan' in borroughs.keys()
assert 2272771 in borroughs.values()
assert ('bronx', 1408473) in borroughs.items()

# tuple
# #####

# tuples are a container type that are immutable and generally used
#   for heterogeneous elements (elements of different type)
# they are immutable in that the elements cannot be changed once
#   the tuple has been created

singers = [('Joplin',  'Janis',   'Port Arthur',  1943),
           ('Gomez',   'Selena',  'Grand Prarie', 1992),
           ('Nelson',  'Willie',  'Abbot',        1933),
           ('Knowles', 'Beyoncé', 'Houston',      1981),]

for surname, name, city, year in singers:
	print name, surname, 'was born in', city, 'in', year

# set
# ###

# sets are like mathematical sets: they are useful for
#   quickly testing for membership and for performing 
#   intersection, union, and difference operations

# elements cannot repeat
female_singers = {'janis joplin', 'janis joplin', 'selena gomez'}
male_singers = {'willie nelson'}
assert len(female_singers) == 2
assert len(male_singers) == 1

# test for inclusion/membership
assert 'janis joplin' in female_singers
assert 'janis joplin' not in male_singers

# calculate the union
assert 'willie nelson' in female_singers | male_singers

# calculate the intersection
assert not female_singers & male_singers

# calculate the difference
singers = {'janis joplin', 'selena gomez', 'willie nelson', 'beyoncé knowles'}
assert singers - female_singers == {'willie nelson', 'beyoncé knowles'}

# str
# ###

# strings are immutable in Python

watchtower = '''"There must be some kind of way out of here," 
Said the joker to the thief, 
"There's too much confusion, 
I can't get no relief."
'''

# test for inclusion
assert 'confusion' in watchtower

# helpful methods for changing case
assert 'confusion'.upper() == 'CONFUSION'
assert 'confusion'.lower() == 'confusion'
assert 'too much confusion'.title() == 'Too Much Confusion'

# use .split to split on a delimiter
assert 'too much confusion'.split(' ') == ['too', 'much', 'confusion']

# use .strip to remove whitespace
assert '   confusion  '.strip() == 'confusion'

# use ' '.join to concatenate strings on a delimiter
assert ' '.join(['too', 'much', 'confusion']) == 'too much confusion'

# int, long, float
# ################

# python has a rich numeric tower, so you usually don't have to worry
#   about the distinction between ints and longs

# note that the largest int you can represent can be found by sys.maxint
from sys import maxint
assert maxint == 2**(64-1)-1 # on 64-bit systems

# we can convert back and forth
assert float(1) == 1.0
assert int(1.0) == 1

# bool & True, False 
# ##################

# None
# ####

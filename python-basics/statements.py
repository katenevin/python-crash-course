# the `if' statement: execute some code conditionally
if True:
    print 'A tautology'

# the `elif' statement: like the if statement, but code only gets
# executed `if' the first if fails
if False:
    print 'We can\'t get here'
elif True:
    print 'Another tautology'

# the `else' statement: our method of last resort
if False:
    print 'Still can\'t get here'
elif 0:
    print '0s are falsy'
else:
    print 'Call this one a not-ology'

# the `while' statement runs some code until a condition is met
mylist = []
while len(mylist) < 10:
    mylist.append(1)
assert len(mylist) >= 10

# the `break' statement gets us out of a loop
mylist = []
while True:
    if sum(mylist) > 10:
        break
    mylist.append(1)
assert sum(mylist) > 10
assert len(mylist) > 10

# the `continue' statement jumps to the next iteration of a loop
sum_of_odds = 0
for i in range(10):
    if not i % 2:
        continue
    sum_of_odds += i
assert sum_of_odds == 25

# the `for' statement lets us iterate over items
cats_in_bag = 0
for i in range(100):
    cats_in_bag += i
assert cats_in_bag == 4950

# the `else' statement, when used with a loop, executes code if `break' isn't called
for i in range(3):
    if i == 10:
        break
else:
    print 'i was never 10'

i = 0
while i < 10:
    if i == 5:
        break
    i += 1
else:
    print 'i was never 5'
assert i == 5

# the `try' and `except' statements let us handle exceptions gracefully
try:
    1 / 0
    print 'Successfully divided 1 by 0'
except ZeroDivisionError:
    pass

try:
    0 / 1
    print 'Successfully divided 0 by 1'
except ZeroDivisionError:
    pass

# the `assert' statement throws an error if the condition is falsy
assert True
try:
    assert False
except AssertionError:
    print 'I don\'t care about assertion errors'

# the `pass' statement is a noop. We can use it as a placeholder.
assert True
try:
    assert False
except AssertionError:
    pass

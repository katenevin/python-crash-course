# importing modules

# the following imports are all valid

import os
import os.path
from os import path
from os import path as p

# you shouldn't do this. It will pollute your namespace, and it might not work
# at all in certain cases. Always be expicit (see: import this).
from datetime import *

# the above is a warning here (and an error in python3):
def myfunc():
    from datetime import *
    assert datetime
    assert date

# this will always fail (comment out this definition to get past it)
def myfun2():
    def inner():
        from datetime import *
        assert datetime
        assert date

import this

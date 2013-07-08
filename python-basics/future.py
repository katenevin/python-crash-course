#!/usr/bin/env python

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

# you may have noticed one of the above lines in the tutorials

# what does it all mean?

# in Python, the __future__ module is a synthetic module. Instead of providing
#   classes and functions for us to use, it provides features. These are often
#   used to provide backward or forward compatible features. The above
#   four imports are used to provide Python 3 features to Python 2 programs.

# the scope of enabling these features is module-only. These features can
#   be enabled in one module and disabled throughout the rest of the system.
#   That way, if you enable a feature that includes a non-backward compatible
#   change, it won't affect system modules.

# note that from __future__ import ... statements must come at the top of the
#   module; these features cannot be enabled inline.

# from __future__ import division
# ###############################

# the `division' feature allows for non-truncating division as the default
#   which matches the standard behavior in Python3

assert 5 / 2 == 2.5 # NOT 2

# to perform a truncating division, use the // operator

assert 5 // 2 == 2 

# from __future__ import print_function
# #####################################

# one of the most notable non-backwards compatible changes in Python 3
#   is that `print` is no longer a statement; it is now a function, 
#   and it requires parenthesis around its argumnets

print('Hello, world!')

# NOT valid:
# print 'Hello, world!'
# print >>file, 'Hello, world!'

# from __future__ import absolute_import
# ######################################

# when you import a module from within a package, it's ambiguous
#   whether the module you want to import is a top-level module or
#   just another module within the package

# the default behavior in Python 2.7 and Python 3 is to see it as a top-level
#   module. This import enables this behavior in Python 2.6 and Python 2.6

# from __future__ import unicode_literals
# #######################################

# in Python 2, there are strings and unicode strings which both derive from
#   a common base class, basestring

# assert type('asdf') is str
# assert type(u'asdf') is unicode
# assert issubclass(str, basestring)
# assert issubclass(unicode, basestring)

# in Python 3, all strings are unicode strings; there is no longer
#   a separate `unicode` class, a `basestring` base class, or the need for
#   the u'' literal syntax

# this feature makes all string literals unicode by default, similar to 
#   Python 3. This can also have the effect of simplifying the str/unicode
#   confusion in Python 2

assert type('asdf') is unicode
assert type(u'asdf') is unicode

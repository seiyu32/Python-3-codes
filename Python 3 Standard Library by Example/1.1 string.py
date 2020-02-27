# string: Text constants and Templates

""" The string module dates from the earliest versions of python. Many of the functions previously
implemented in the module have been moved to methods of str objects, but the module retains several
useful constants and classes for working with str objects. This discussion will concentrate on them. """

# 1.1 Fucntions
# The function capwords() capitalizes all of the words in a string.

import string

s = 'The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

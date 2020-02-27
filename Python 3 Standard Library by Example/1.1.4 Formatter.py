"""
The formatter class implements the same layout specification language as the format()
method of str. Its features include type coersion, alignment, attribute and field references,
named and positional template arguments, and type-specific formatting options. Most of the
time the format() method is a more convenient interface to these features, but Formatter
is provided as a way to build subclasses, for cases where variations are needed.
"""

# 1.1.5 Constants

# The string module includes a number of constants related to ASCII and numerical character sets.
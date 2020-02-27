# Compiling Expressions

# Although re includes module-level functions for working with regular expressions as text
# strings, it is more efficient to compile the expressions a program uses frequently. The
# compile() function converts an expression string into a RegexObject.



import re

# Precompile the patterns.
regexes = [
    re.compile(p)
    for p in ['this', 'that']
]
text = 'Does this text match the pattern?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print('Seeking "{}" ->'.format(regex.pattern),
          end=' ')

if regex.search(text):
    print('match!')
else:
    print('no match')
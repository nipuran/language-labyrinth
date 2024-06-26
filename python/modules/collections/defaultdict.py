'''
A Defaultdict is also a sub-class to dictionary. It is used to provide some
defualt values for the key that does not exist and never raise a KeyError.
'''

from collections import defaultdict

mydict = defaultdict(list)

# Access a non-existent key
print(mydict['a']) # {'a': []}
print(mydict['b']) # {'b': []}

#------
print()
#------

# Append a value
mydict['a'].append(1)
print(mydict)
mydict['b'].append(3)
print(mydict)

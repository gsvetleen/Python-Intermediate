# If a name has an underscore, we should not be changing without a good reason.
# There are no such thing as private methods in pythons. You use underscores
# to indicate intention

import shelve

print(dir())

# __Builtin__ -> Python Interpreter has already built in functions available

print(dir(__builtins__))

# methods in builtin
for m in dir(__builtins__):
    print(m)

# methods in shelve
for m in dir(shelve):
    print(m)

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# help()->prints out information on how to use a particular library object
help(shelve)

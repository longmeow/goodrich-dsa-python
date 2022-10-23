'''C-1.16 In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] = factor. We have discussed that numeric
types are immutable, and that use of the = operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?

def scale(data, factor):
    for j in range(len(data)):
        data[j] = factor
'''


'''Nah, the scale function doesn't change the actual parameter sent by the caller, it just 
expands the command to data[j] = data[j] * factor then assign to data[j]'''


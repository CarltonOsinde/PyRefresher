#advanced functions

#Having two parameters in your custom function


def area(a,b):
    return a*b

print(area(1,2))


#Arbituary Numbers & Non-Keyword arguments ~ ALWAYS INPUT THE *
#THIS WILL OUTPUT THE ARGUMENTS AS A TUPLE

def mean1(*args):
    return args

#if you call it as is the function will return a TUPLES


def mean(*args):
    return sum(args)/len(args)

print(mean(1,3,4,6)) 


#KEYWORD ARGUMENTS ~ ALWAYS INPUT THE **


def key_words(**kwargs):
    return kwargs


print(key_words(name="Carlton", income = 2100000, age = 23, status="High-Value"))

username_database = {}
username_database.update(key_words(name="Carlton", income = 2100000, age = 23, status="High-Value"))

print(username_database.items())
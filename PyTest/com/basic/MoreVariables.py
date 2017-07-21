'''
Created on 07-Mar-2017

@author: srayabar
'''
my_name = "srinath"
my_age = 31
my_place = "pasara"

# %d is for numbers and %s for strings
# for more characters : https://docs.python.org/2.4/lib/typesseq-strings.html

print "Hello, this is %s and he's %s years old. He is from %s" % (my_name, my_age, my_place)

print "Hello, this is %r and he's %r years old. He is from %r" % (my_name, my_age, my_place)

w = "this is something %s"
e = "new"

print w % e 
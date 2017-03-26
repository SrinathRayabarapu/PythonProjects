'''
this is with Regular expressions

Author : Srinath R
'''

import re

phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumberRegex.search("Hey, my number is 123-456-7890, and not 451-782-2001!")
print "Phone numbers found are ", mo.group()
print phoneNumberRegex.findall("Hey, my number is 123-456-7890, and not 451-782-2001!")


phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumberRegex.search("Hey, my number is 123-456-7890, and not 451-782-2001!")
print "Phone numbers found are ", mo.group(1)
print "Phone numbers found are ", mo.group(2)


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search("Batman's Batmobile lost a wheel")
print "Searched regex are -", mo.group()
print "Searched regex are -", mo.group(1)




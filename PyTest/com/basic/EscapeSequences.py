tabby_cat = "\tI'm tabbed in!"
persian_cat = "I'm splitting\nin line!"
backslash_cat = "This is \\a backslash \\text"
#this is the way to write free flowing text
fat_cat = """
hey\n\t* i'm a fat cat
    * with some random text!!
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "%r" % fat_cat

print '''sdjskdjskdjsk

sldsdjks \n aaaa
skdskjd
        sdskdjsk
'''

'''
while True:
    for i in ["/","- ","|","\\","|"]:
        print "%s\r" % i,
'''

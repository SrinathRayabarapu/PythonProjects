'''
about reading and writing files
'''

fileName = raw_input("Hey, what file you want me to open? ")
txt = open(fileName)

print "Here's your text\n", txt.read()

txt.close()

#below line doesn't work
#print txt.read()
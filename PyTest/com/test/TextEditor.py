'''
about reading files and truncating their text and writing new text to it
'''

fileName = raw_input("Enter file name that you want to erase? ")
fileName = fileName + '.txt'

decision = raw_input("Sure you want to erase? ")

if decision == "y":
    target = open(fileName, 'w')

print "Truncating file, tata!"
target.truncate()

text = raw_input("Enter text that you want to write to file - ")
target.write(text)

print "almost done..."
target.close()
'''
program to check given text is a phone number or not

author : Srinath R
'''


def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdigit():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdigit():
            return False
    else:
        # default is True
        return True

print "9916149606 is a Landline number ?"
print isPhoneNumber('9916149606')

print "123-456-7890 is a Landline number ?"
print isPhoneNumber('123-456-7890')

print "458-981-54712 is a Landline number ?"
print isPhoneNumber('458-981-54712')

bigText = "Hey, my number is 123-456-7890, and not 451-782-2001!"
for i in range(len(bigText)):
    chunk = bigText[i:i + 12]
    if isPhoneNumber(chunk):
        print "Phone number found : " + chunk
print "Done!"

#!usr/bin/python

class MyClass:
    #constructor
    def __init__(self):
        print "This is called from Constructor init"
        self.x = 100;
        self.y = 200;

    def printMemberVariables(self):
        print ("X value is : ", self.x)
        print ("X value is : ", type(self.y))
        print self.x + self.y

def main():
    obj1 = MyClass()
    obj1.printMemberVariables()

if __name__ == "__main__":
    main()
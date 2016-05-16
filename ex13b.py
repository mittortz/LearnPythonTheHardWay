from sys import argv

script, first, second = argv

name = raw_input("What is your name?")

print "Your script name is %s and your name is %s." % (script, name)
print "I don't know why you gave me the arguments:", first, second

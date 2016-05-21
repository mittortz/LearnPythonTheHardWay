# adds 'argv' module to accept additional arguments
from sys import argv

# assigns variable names to arguemnts received through 'argv'
script, filename = argv

# assigns variable name to 'open' function for argument 'filename'
txt = open(filename)

# prints name of file
print "Here's your file %r:" % filename

# reads file and prints contents
print txt.read()

# prompts user to enter filename again
# print "Type the filename again:"
# file_again = raw_input("> ")

# assigns new variable name to 'open' function for new filename
# txt_again = open(file_again)

# reads file again using new variable and prints contents
# print txt_again.read()

txt.close()

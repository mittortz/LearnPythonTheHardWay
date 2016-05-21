from sys import argv

script, input_file = argv

# defines function to read the file and print it entirely
def print_all(f):
    print f.read()

# defines function to set reading position to zero
def rewind(f):
    f.seek(0)

# defines function to print a single line from the file, starting wherever
# the reading position is
def print_a_line(line_count, f):
    print line_count, f.readline()

# declares file object (DVD player) for the file
current_file = open(input_file)

# calls the print_all function to display entire file
print "First let's print the whole file:\n"

print_all(current_file)

# calls function to reset reading position to zero
print "Now let's rewind, kind of like a tape."

rewind(current_file)

# calls function to read and print individual lines from file
# each time function is called, reading position moves up
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# calls function to close file
current_file.close()

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# in_file = open(from_file)
# indata = in_file.read()

# as one line:
indata = open(from_file).read()

# print "The input file is %d bytes long." % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CTRL-C to abort."
# raw_input()



out_file = open(to_file, 'w').write(indata)
# out_file.write(indata)

print "Alright, all done."

# file does not need to be closed due to line 21 open/write method
# out_file.close()

# file does not need to be closed due to line 13 open/read method
# in_file.close()

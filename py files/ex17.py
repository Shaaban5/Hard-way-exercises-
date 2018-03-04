from sys import argv
from os.path import exists

script, from_file, to_file = argv

print 'copying from %s to %s' % (from_file, to_file)

file_open=open(from_file)
data=file_open.read()

print 'the input file is %d bytes long' % len(data)

print 'does the output file exists? %r' % exists(to_file) # true or false

raw_input('if you ready press enter>')

output_file=open(to_file, 'w')
output_file.write(data)

output_file.close()
file_open.close()
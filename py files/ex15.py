from sys import argv

script, filename = argv

print 'Here we are printing %r' % filename
text = open(filename) # assign class to file name
print text.read()	  # use text.read() function to print it
text.close()

# using raw.input()

text_again=open(raw_input('Tell me file name to read it for you:> '))
print text_again.read()
text_again.close()
from sys import argv

script, filename = argv

def print_all(file):
	print file.read()

def rewind(file):
	file.seek(0)  # VERY IMP: u can think abt it like a tape need to start from beggining after u read *listen*

def print_a_line(line_count, file):
	print line_count, file.readline() # read line after line and if u need from bigging u must use above .seek(0)
			# .readline() each time i used it print \n after it read line to prvent it add ,(comma) after the print			

current_file=open(filename)

print 'lets print it all first: \n'
print_all(current_file)

print 'lets rewind: \n'
rewind(current_file)

print 'print line by line: \n'
current_line = 1 
print_a_line(current_line, current_file)
current_line += 1 
print_a_line(current_line, current_file)
current_line += 1 
print_a_line(current_line, current_file)
'''
open('filename', access mode , buffering )
access mode : 
- 'r' (read only) the defualt access mode, pointer at the beginning of file
- 'r+' (reading & writing) pointer at the beginning of file but doesnt create new file if not exist
- 'w' (writing only) Overwrites if file exist or create new file not folder, always remove old date to start clean
- 'w+' (writing & reading) Overwrites if file exist or create new file
- 'a' (appending file) pointerat the end of file
- 'a+' (appending & reading)
'''
new_text = open('test text.txt', 'w+') # w & w+ mode require write() as it remove all date in file if exist
# it better to use r+ as it doesnt remove date but if data were givien it will act just like w mode

print new_text.name # return file name
print new_text.mode # return the access mode of the file
print new_text.closed # return F if file still open, T if file closed

new_text.write('again this a test wrinting inside text file by write method through python\n')
# in this situation pointer at the end use .seek() to return back to first
new_text.writelines(['line2\n', 'line2\n', 'line3\n']) # add severl line from list 

print new_text.tell() # return my current position place
new_text.seek(0)	  # chagne pointer position to the given byt num
print new_text.tell()

print new_text.read() # .read() start reading from the current position to the given byt num. ex: read(10)
new_text.seek(0)

print new_text.next() # read only 1 line and add empty line after reading then if method repeated it reads next line 7 so on
print new_text.next() # if lines finish it gives error (next()used in loops)

new_text.seek(0)
print new_text.readline() # read only 1 line and add empty line after reading then if method repeated it reads next line 7 so on
# when lines finish it gives empty

# new_text.truncate() # earse the rest of data after the current position

new_text.seek(0)
print new_text.readlines() # return a list contain each line in 1 element

new_text.close() # this close the file again
print new_text.closed
'______________________________________________'
import os, sys
os.remove('renamed file.txt') # delete file with (given name)
os.rename('test text.txt', 'renamed file.txt') # rename (given name , to new name)
#os.renames('old file', 'new folder/new file name') # move and chage file name (from, to )

os.mkdir('new folder') # creates new dirc (given folder name)
os.rmdir('new folder') # delete empty folder only

'''
with open('new folder/test.py' , 'w') as f :
	f.write('#wow .. if u can read this, this is amazing')
	f.close()												'''

print os.getcwd() # return current working dirc address
# better to save the getcwd to var original_path = os.getcwd()
# os.chdir(r'C:\Users\secretary-1\Udacity') # change working dirc to (given address)
# os.fchdir(r'open file path') # it change cwd to the dirc of the openned file

print os.access('test text.txt', os.F_OK) # access('path', os.F_OK) check if file exist
# check online for more option and other methods to change files & folder permissions
# chown() chflags() chmod() and a lot other methods

fd = os.open(r'renamed file.txt',os.O_RDWR) # open file as read & write
os.write(fd, 'add line by os.write')
os.lseek(fd,0,0) # just like .seek() but give ('openned file', 0, 0)
print os.read(fd,5555) # read ('file openned', max num of byt)
os.close(fd)

print os.listdir(r'C:\Users\secretary-1\Udacity\my-exercise\my work') # return a list with all files & folder name in the given path
os.startfile('renamed file.txt')

print os.path.split(r'C:\Users\secretary-1\Udacity\my-exercise\my work\renamed file.txt')
# os.path.split(r'path') split the path to 2 arguments tree and file name (or last folder name)


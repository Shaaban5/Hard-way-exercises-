import webbrowser
from webbrowser import Chrome # used to call Chrome class by using .register('name', Class name)

#webbrowser.open(r'www.google.com',0) # open url
#webbrowser.open_new(r'www.google.com')
print webbrowser.register('chrome',	Chrome('chrome')) # here we confirm using chrome by using Chrome class

#google = webbrowser
#google.open(r'www.google.com')

'______________________________________________'
import urllib # in urllib must use the full address name http://www......

print urllib.urlopen(r'http://www.google.com').read(5) # .read() & .readline() & .readlines() could be used
urllib.urlretrieve(r'http://www.google.com','text.html') # copy HTML of the given site to a given name file
print urllib.getproxies() # return a proxy if it was given

response = urllib.urlopen(r'http://www.google.com')
print response.geturl()

headers = response.info()
print 'DATE    :', headers['date']

print urllib.urlopen(r'http://www.wdylike.appspot.com/?q=shit and shot').read()

happynumbers = urllib.urlopen(r'http://www.practicepython.org/assets/happynumbers.txt')
happylist = happynumbers.read().split() # make a list for the web page openned

# or could be 1 line as follow
primenumberss = urllib.urlopen(r'http://www.practicepython.org/assets/primenumbers.txt').read().split()


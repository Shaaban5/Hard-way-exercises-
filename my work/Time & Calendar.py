import time

print time.time() # return secs sinsce 12 am 1/1/1970 this called epoc
print time.localtime() # takes nothing for current time ot given secs and current 9 tupletime (wday# start from 0 monday)
print time.gmtime() # takes secs gives GM time by localtime() formate
print time.ctime() # same asctime() but takes secs then gives regulare formatted time


print time.mktime([2009, 1, 1, 0, 0, 0, 0, 0, 0]) # opposit if localtime() as takes 9 tupletime and return secs
print time.asctime([2009, 1, 1, 0, 0, 0, 2, 0, 0]) # takes nothing for current or 9 tupletime and 
# return regualr formatted time (day name mm dd 24_hr_time yyyy) 

time.sleep(0) # sys sleep for given secs then contiue printing after the secs 

print time.strftime('%H',time.localtime()) # takes str only for current or str and given 9 tupletime return time formated as u given
# % a'A day b'B month y'Y yr(shrt'ful name)
#%d/%m/%y  day month year numbers = %x for date but mm/dd/yy %X represent time only
# %U wk# in year %j day of year %z time zone name
# %c date and time %H hr in 24

print time.strptime('21 november 2015 00:05:05', '%d %B %Y %X') # takes 2 str and return 9 tupletime
# strptime(str'must be euqal to given %formate' , str'given %formate')

t = [2009, 1, 1, 0, 0, 0, 0, 0, 0]
print time.strftime('%d/%m/%Y\t%X',t) 
'______________________________________________'
import calendar

calendar.calendar(2000) # print calendar of givien year 
print calendar.month(2018, 10) # print out month calendar
print calendar.isleap(2016) # check leap year return True or False
print calendar.leapdays(2000,2018) # print no. of leap days btw 2 given years
print calendar.weekday(2018,3,14) # return weekday code of the given date (0=monday)

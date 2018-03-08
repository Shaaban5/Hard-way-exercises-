print True and True # T
print False and True # F
print 1 == 1 and 2 == 1 # F
print "test" == "test" # T
print '\n'
print 1 == 1 or 2 != 1 # T
print True and 1 == 1 # T
print False and 0 != 0 # F
print True or 1 == 1 # T
print '\n'
print "test" == "testing" # F
print 1 != 0 and 2 == 1 # F
print "test" != "testing" # T
print "test" == 1 # F 
print '\n'
print not (True and False) # T
print not (1 == 1 and 0 != 1) # F
print not (10 == 1 or 1000 == 1000) # F
print not (1 != 10 or 3 == 4) # F
print '\n'
print not ("testing" == "testing" and "Zed" == "Cool Guy") # T
print 1 == 1 and not ("testing" == 1 or 1 == 0) # T
print "chunky" == "bacon" and not (3 == 4 or 3 == 3) # F
print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") # F
print '\n'
print 'test' <= "test" # T # QUOTE OR DOUBLE Q DOESNT AFFECT
print 'test' <= 'testI' # T
print 'test' <= 'test-ING' # T # CHECK SAME ORDER AND THEN COMPARE
print 'test' <= 'ING-test' # F # order is important
print '\n'
print True and 'aaaaaaa' # 1st check right side if true check left side then return last one checked
print False and 'aaaaaaa' # 1st check right side found false then return false without checked left side
print 'aaaaaaa' and True ,'\t', 'aaaaaaa' and False # it hase to check the left side
print '\n'
print True or 1  # the oppist in 'or' 1st check right side if rtuen true and doesnt check left side
print False or 1 # 1st check right side if false check left side and return last one checked
print 1 or False,'\t',1 or True # doesnt have to check the left side

print any and True , any and False
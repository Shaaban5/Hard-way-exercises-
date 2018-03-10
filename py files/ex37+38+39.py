region = { 				# elements here called key
	'Riyadh' : 'RYD' ,
	'Makkah' : 'MK' ,
	'Madina' : 'MD' ,
	'Estren' : 'EST' ,
	'Tabuk' : 'TB'
}

cities = {
	'MK' : 'jeddah' ,
	'MD' : 'yanbu' ,
	'EST' : 'damam'
}

cities['RYD'] = 'in ry'
cities['TB'] = 'in tb'

print 'citi in Makkah is:', cities['MK']
print 'another way:' , cities[region['Makkah']]

print 'Riyadh abberivation is:' , region['Riyadh']

#using dict in loop, transfer dict to list by .items()
for reg , abber in region.items():
	print 'region is %s and abber is %s and beggest city is %s' % (reg, abber, cities[abber])

print region.items() 
dict_to_list = region.items() 
print dict_to_list[0]

print region.get('Riyadh') # .get() here just return the value of named key
print region.get('Hail', None ) # .get(new key , value or None) return here a value or None for key that doesnt exist

print region
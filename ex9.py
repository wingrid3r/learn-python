weekFormatter = "%s " * 7
monthFormatter = "%s\n" * 12

print "Here are the days :" + weekFormatter % ('Sun', 'Mon', 'Tue', 'Wed', 
	'Thu', 'Fri', 'Sat')
print "Here are the months : " + monthFormatter % ('Jan', 'Feb', 'Mar', 
	'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
	
# Another way
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:" , days
print "Here are the months:" , months
 
print """
 This cane be a string with any lines.
 By any line I meant absolutely any number of lines.
 See it yourself.
 don't you believe that?
 """
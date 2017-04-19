from sys import argv
#get command line arguments
scriptName, fileName = argv
#open file in read mode and display the contents
print "Erasing contents of file - %s" %fileName
#print "File contents are displayed below\n%s\n%s" % ('*' * 80, 
#	open(fileName).read())
#open file for writing
print "Hit CTRL-C (^C) to CANCEL or Hit Enter to CONTINUE"
raw_input("What is it going to be? ")
print "Opening the file..."
fileObj = open(fileName, 'w')
#erase file contents
print "Truncating the file..."
fileObj.truncate()
#get new input lines
print "\nPlease input your 3 lines\n%s" % ('-' * 80)
line1 = raw_input('Line1: ')
line2 = raw_input('Line2: ')
line3 = raw_input('Line3: ')
#write new contents to file
print 'Writing new contents to file...'
fileObj.write(line1 + '\n' + line2 + '\n' + line3)
#close the file
print 'Closing the file...'
fileObj.close()
#re-open the file and display the new contents
print "\nNew file contents are displayed below\n%s\n%s" % ('#' * 80, 
	open(fileName).read())
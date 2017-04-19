from sys import argv

#get command line arguments (in this case, the file name)
scriptName, fileName = argv
#open the file
txt = open(fileName)
#read and display the file contents
print "Contents of the file - %s is displayed below:\n%s" % (fileName, 
	'*' * 55)
print txt.read()
#close file
txt.close()

#another try
fileNameAgain = raw_input('Type the File Name: ')
txtAgain = open(fileNameAgain)
print "%s file contains...\n%s" % (fileNameAgain, 	
	txtAgain.read())
txtAgain.close
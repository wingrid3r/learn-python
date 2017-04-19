from sys import argv

#method to copy file contents. Will overwrite if file exist
#or create new file if file does not exist
def copyFile(f1, f2):
	open(f1, 'w').write(open(f2).read())

#append to existing file content	
def extendFile(f1, f2):
	open(f1, 'a').write(open(f2).read())

#get command line inputs	
scriptName, file1, file2 = argv
#prompt user to enter file name
newFile = raw_input("Enter new file name: ")

#invoke the methods
copyFile(newFile, file1)
extendFile(newFile, file2)

#print new file contents
print "Contents of new file %s is given below:\n%s" % (newFile, 
	open(newFile).read())
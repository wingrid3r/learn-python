from sys import argv
#capture command line arguments
scriptName, inputFileName = argv
#method to print contents of a file
def printAll(f):
	print f.read()
#resets the file position to BOF	
def rewind(f):
	f.seek(0)
#method to print a line from a file	
def printALine(lineNum, f):
	print lineNum, f.readline(),
#open the file
currentFile = open(inputFileName)

print "Print contents of the file - %s\n" %(inputFileName)	
printAll(currentFile)
print "Rewind file.\n",
rewind(currentFile)

print "Print 3 lines from this file.\n",
currentLine = 1
printALine(currentLine, currentFile)
currentLine += 1
printALine(currentLine, currentFile)
currentLine += 1
printALine(currentLine, currentFile)
#reset the file
rewind(currentFile)
currentLine += 1
printALine(currentLine, currentFile)

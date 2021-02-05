# PSC analyse text Q1ofAssgn1.txt
# enter name of file
# determine number of lines, words and characters in the file

def main():
    filename = raw_input ("Enter the file name to open: ") #assign variable1 filename to the user input
    
    infile = open(filename, "r") #assign variable2 infile to opened file
    data = infile.read() #assign variable3 data to read version of infile

    words = data.split() #assign variable4 words for split version of data
    chars = list(data) #assign variable5 chars for individual characters of data

    countLines = len(open(filename, 'rU').readlines()) #
    countWords = len(words)
    countChars = len(chars)
    
    print "In this textfile, the number of: "
    print "lines is: ", countLines
    print "words is:  ", countWords
    print "characters is: ", countChars

main()
    

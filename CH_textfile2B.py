# PSC analyse text Q1ofAssgn1.txt
# enter name of file
# determine number of commas in text file

def main():
    filename = raw_input ("Enter the file name to open: ")
    
    infile = open(filename, "r")
    data = infile.read()

    words = data.split()
    chars = list(data)

    countLines = len(open(filename, 'rU').readlines())
    countWords = len(words)
    countChars = len(chars)
    countComma = chars.count (",")
        
    print "In this textfile, the number of: "
    print "lines is: ", countLines
    print "words is:  ", countWords
    print "characters is: ", countChars
    
    if countComma >= 1:
        print "commas is: ", countComma

main()
    

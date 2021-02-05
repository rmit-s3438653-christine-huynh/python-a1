# PSC analyse text Q1ofAssgn1.txt
# enter name of file
# find and count the word user inputs

def main():
    filename = raw_input ("Enter the file name to open: ")
    w1 = raw_input ("Enter the word you wish to find in the textfile ")
    
    infile = open(filename, "r")
    data = infile.read()

    words = data.split()

    found = words.count(w1)

    if found >= 1:
        print found
    else:
        print "not found",
main()
    

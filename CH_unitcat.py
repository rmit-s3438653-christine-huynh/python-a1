# PSC combine two txt
# output as new file

def main():
    print "program to combine two txt files"

    coFile = open ("Unitcode.txt", "r")
    unitdata = coFile.read()
    unitcut = unitdata.split(u)

    naFile = open ("Unitname.txt", "r")
    namedata = naFile.read()
    namecut = namedata.split(n)
    
    outFile = open("mit.txt", "w")
    
    
    for line in inFile:
        code, name = string.split(line)
        output = code + name

        outfile.write(code + '/n')

    infile.close()
    inFile2.close()

    print "the combined file is: ", mit.txt

main()

import sys
import os
import codecs

def validArgs():
    return os.path.isfile(sys.argv[1]) and len(sys.argv)>=2

def getFile():
    if(validArgs()):
        return sys.argv[1]
    else:
        print("Invalid argument, check input")
        sys.exit(0)

def outputFileAsBytes(input_file):
    file_length = os.path.getsize(input_file) 
    with open(input_file, "rb") as f:
        block = f.read()
        if(block):
            return block
        else:
            print("file is invalid, check input")
            sys.exit(0)
            
def main():
    index = 0
    string = ""
    hexify = codecs.getencoder('hex')
    input_file = getFile()
    file_bytes = outputFileAsBytes(input_file)
    hex_string = []
    output_file = sys.argv[1] + "_output.txt"
    if(len(sys.argv)==3):
        output_file = sys.argv[2]

    for b in file_bytes:
        if index%16 == 0:
            print(format(index, '06X'), end=' ') 
            print(hex(b), end=' ')
            string += format(index, '06X')
            string += " "
            string += hex(b)
            string += " "

        elif index%16 == 15:
            print(hex(b))
            string += hex(b)
            string += " "
            hex_string.append(string)
            string = ""
        else:    
            print(hex(b), end=' ')
            string += hex(b)
            string += " "
            
        index += 1
         
    hex_string.append(string)
    print("")
    
    with open(output_file, "w+") as f:
        for line in hex_string:
            f.write(line + "\n")


main()

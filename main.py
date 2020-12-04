import sys
import os
import codecs
import binascii

def validArgs():
    return os.path.isfile(sys.argv[1]) and len(sys.argv)==2

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
    data = ""

    for b in file_bytes:
        if index%16 == 0:
            print(format(index, '06X'), end=' ') 
            print(hex(b), end=' ')
        elif index%16 == 15:
            print(hex(b))
        else:    
            print(hex(b), end=' ')

        hex_string.append(format(b, 'x'))
        index += 1
    
    print("")
    data = data.join([str(elem) for elem in hex_string])
    data = data.replace(' ', '')
    data = data.replace('\n', '')
    data = data.strip()
    data = data[:-1]
    print(data)
    data = binascii.a2b_hex(data)
    with open("output_file.jpg", "wb") as output_file:
        output_file.write(data)

main()

import binascii
import struct
import sys
f = open(sys.argv[1],'rb')
text_file = open("utf8encoder_out.txt", "wb")
while True:
    byte1 = f.read(1)
    if not byte1:
         break
    #byte one in decimal
    c1 = int(binascii.hexlify(byte1), 16)
    #byte two in decimal
    byte2 = f.read(1)
    if not byte2:
        c2 = 0
    else:
        c2 = int(binascii.hexlify(byte2), 16)
    c3 = (c1<<8) | c2

    charBin = bin(c3)
    charBin = charBin[2:]
    lenChar = len(charBin)

    if lenChar <= 7:
        utf8Char = '0' + charBin.zfill(7)
        _utf8Char = chr(int(utf8Char,2))
        #print _utf8Char
        text_file.write(_utf8Char)
    elif lenChar <= 11:
        firstByte = '1' + '0' + charBin[-6:]
        filledString = charBin.zfill(11)
        secondByte = '1' + '1' + '0' +filledString[0:5]
        _utf8char = chr(int(secondByte,2)) + chr(int(firstByte,2))
        #print _utf8char
        text_file.write(_utf8char)
    elif lenChar <= 16:
        firstByte = '1' + '0' + charBin[-6:]
        secondByte = '1' + '0' + charBin[-12:-6]
        filledString = charBin.zfill(16)
        thirdByte = '1' + '1' + '1' + '0' +filledString[0:4]
        _utf8Char16 = chr(int(thirdByte,2)) +  chr(int(secondByte,2)) +chr(int(firstByte,2))
        #print _utf8Char16
        text_file.write(_utf8Char16)
text_file.close()
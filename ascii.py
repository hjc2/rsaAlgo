




m = "Hello"


def encodeAscii(m):
    text = ''
    for x in m:
        organ = str(ord(x))
        if(len(organ) == 1):
            organ = "90" + organ
        if(len(organ) == 2):
            organ = "9" + organ
        text = text + organ
    return(text)

def decodeAscii(m):
    # Iterate over the string in steps of 3
    number_str = str(m)
    text = ''
    for i in range(0, len(number_str), 3):
        three_digits = number_str[i:i+3]
        three_digits_int = int(three_digits) % 900
        
        text = text + chr(three_digits_int)

    return(text)
    

print(encodeAscii(m))

message = encodeAscii(m)

print(decodeAscii(message))
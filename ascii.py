

m = "Hello127438244"

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
        text = text + chr(int(number_str[i:i+3]) % 900)

    return(text)
    

message = encodeAscii(m)

print(decodeAscii(message))
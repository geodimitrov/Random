def decipher(cipher):
    result = ''
    start_i = 0
    
    for i in range(len(cipher)):
        n = int(cipher[start_i: i+1])

        if n > 96:
            result+= chr(n)
            start_i = i + 1
        

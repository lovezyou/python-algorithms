uppercase = ['','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase = ['','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(words, key):
    cipher = []
    cipher_word = []
    cipher_list = ""
    
    for word in words :
        for letr in word :
            val = 0
            if letr in uppercase :
                val = int(uppercase.index(letr))+key
                if val > 26: val = val - 26
                elif val < 0 : val = 26 + val
                elif val == 0 : val = 26
                cipher.append(uppercase[val])
        
            elif letr in lowercase :
                val = int(lowercase.index(letr))+key
                if val > 26: val = val - 26
                elif val < 0: val = 26 + val
                elif val == 0: val = 26
                cipher.append(lowercase[val])
            else :
                cipher.append(letr)
        cipher_word.append("".join(cipher))
        cipher = []
    
    cipher_list = " ".join(cipher_word)
    print(cipher_list)
            
            
words = input("Enter string : ").split()
key = int(input("Enter key : "))
caesar(words, key)

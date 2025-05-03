#
# Jay 
# 4/26/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#The Encryption Library
encryption_library = {'A': '%', 'a' : '9', 'B' : '@', 'b' : '#', 'C' : '(', 'c' : '<', 'D' : '!', 'd' : '[', 'E' : '#', 'e' : '}',
                        'F' : '}', 'f' : '&', 'G' : '^', 'g' : ']', 'H' : '*', 'h' : '(', 'I' : '=', 'i' : '+', 'J' : '-', 'j' : '_',
                        'K' : '"', 'k' : ';', 'L' : ':', 'l' : "'", 'M' : '<', 'm' : '>', 'N' : '?', 'n' : '/', 'O' : ',', 'o' : '.',
                        'P' : '>', 'p' : '<', 'Q' : '|', 'q' : '`', 'R' : '~', 'r' : '{', 'S' : '}', 's' : '[', 'T' : ']', 't' : '^',
                        'U' : '&', 'u' : '*', 'V' : '(', 'v' : ')', 'W' : '-', 'w' : '_', 'X' : '+', 'x' : '=', 'Y' : ':', 'y' : ';',
                        'Z' : '@', 'z' : '#',} 

#Opening the Plain flie and Encryption
with open("Plain_text_File.txt', 'r'") as orig_file:
    file_read = orig_file.read()
with open('Encrypted_Plain_Text_File.txt', 'w') as encrypt_file:
    for ch in file_read: #Loop
        encrypt_file.write(encryption_library.get(ch, ch))
#Decryptioning 
with open('Encrypted_Plain_Text_File.txt', 'r') as encrypt_file:
    file_read = encrypt_file.read()

decryption_libary = {v: k for k, v in encrypt_file.items()}
for ch in file_read: #Loop
    print(decryption_libary.get(ch, ch), end='')

#The Decryption Library
decryption_library = {v: k for k, v in encryption_library.items()}

orig_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = orig_file.read()
orig_file.close()
encrypt_file = open('DECRYPTED_Plain_Text_File.txt','w')

for ch in file_read: #Loop
    if ch in decryption_library:
        encrypt_file.write(decryption_library[ch])
    else:
        encrypt_file.write(ch)

encrypt_file.close()
encrypt_file = open('ENCRYPTED_Plain_Text_File.txt','r')
file_read = encrypt_file.read()
encrypt_file.close()    
codes_items = decryption_library.items()

for ch in file_read:
    if not ch in decryption_library.values() or ch == '.' or ch == ',' or ch == '!':
        print(ch)
    else:
        for k,v in codes_items:
            if ch == v and ch != '.':
                print(k,end='')







   

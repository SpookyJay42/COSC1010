#
# Jay 
# 4/26/2025
# File Encryption and Decryption Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

#The Encryption Library
encryption_library = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(',
                      'J':')','K':'-','L':'_','M':'+','N':'=','O':'`','P':'~','Q':'{','R':'[',
                      'S':'}','T':']','U':':','V':';','W':'"','X':'<','Y':'>','Z':'0','a':'1',
                      'b':'2','c':'3','d':'4','e':'5','f':'6','g':'7','h':'8','i':'9','j':'a',
                      'k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'}
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






   

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caefer(text,shift,direction):
    newtext=""
    if direction=="decode":
        shift*= -1
    for letter in text:
        pos=alphabet.index(letter)
        newpos=pos+shift
        newletter=alphabet[newpos]
        newtext+=newletter
    print(f"your {direction}d result :- {newtext}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
caefer(text,shift,direction)



# def encrypt(text,shift):
#   encryptedtext=""
#   for letter in text:
#     pos=alphabet.index(letter)
#     newpos=pos+shift
#     newletter=alphabet[newpos]
#     encryptedtext+=newletter
#   print(f"Your secret message is {encryptedtext}")

# def decrypt(text,shift):
#   decryptedtext=""
#   for letter in text:
#     pos=alphabet.index(letter)
#     newpos=pos-shift
#     newletter=alphabet[newpos]
#     decryptedtext+=newletter
#   print(f"Original text is {decryptedtext}")



# if direction=="encode":
#   encrypt(text,shift)
# else:
#   decrypt(text,shift)
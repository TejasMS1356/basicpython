import random
import string
char=string.digits+string.ascii_letters+string.punctuation+" "
char=list(char)

key=char.copy()
random.shuffle(key)
#encryption
message=input("enter the message: ")
cipher_text=""
for letter in message:
    index=char.index(letter)
    cipher_text+=key[index]
print(f"entered message is:{message}")
print(f"encrypted message is:{cipher_text}")


#decryption
chiper_text=input("enter encrypted message: ")
message=""
for letter in chiper_text:
    
    index=key.index(letter)
    message+=char[index]
print(f"encrypted message is {cipher_text}")
print(f"decryped message is:{message}")


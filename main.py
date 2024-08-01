from encode import Encode
from decode import Decode

print("Welcome to the Hex Encoder!")
inp = input("Enter E to Encode and D to Decode:")
if inp == 'E' or inp == 'e':
    print("Enter text that needs to be encoded:", end=" ")
    str_inp = input("")
    enc = Encode()
    encoded_str, key = enc.str_enc(s1=str_inp)
    print("Encoded text: "+encoded_str)
    print("Key:" + key)


elif inp == 'D' or inp == 'd':
    print("Enter text that needs to be decoded: ", end="")
    txt_inp = input("")
    print("Enter KEY of the text that needs to be decoded: \n")
    key_inp = input("")
    dec = Decode()
    txt_op = dec.hex_to_str(txt_inp, key_inp)
    print("Text is:", txt_op)


else:
    print("Enter proper values...")

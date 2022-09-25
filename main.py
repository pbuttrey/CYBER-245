# Paige Buttrey
# Vigenere Cipher
import random
import sys
# This function generates the
# key in a cyclic manner until
# it's length isn't equal to
# the length of original text
def generateKey(keySize):
    key = []
    for i in range(keySize):
        key.append(chr(random.randomrange(26)+ord('A')))
    return ("".join(key))


# This function returns the
# encrypted text generated
# with the help of the key
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))



if __name__ == "__main__":
    if len(sys.argv) !=2:
        print(len(sys.argv))
        print("Wrong number of commandline arg. Command format is: python keygen keysize")
        sys.exit(1)
    if int(sys.arg[1]) <1:
        print("Keysize should be 0<")
        sys.exit(1)
    print(generateKey(int(sys.argv[1])))

# Get HTML file to encrypt

def get_HTML_enc():

# Open file and read it
    f = open("myfile.html", "r")
# Encrypt the file

# Print the file you are reading
    content = f.read()
#Letter by letter using key to encrypt

# Close the file
    f.close()

    return content

#get_HTML()

def get_HTML_dec():
    f = open("myfile.html", "r")
#decrypt file

    new_content = f.read()
#close file
    f.close()
# get file
    return new_content
# get_HTML()



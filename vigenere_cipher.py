# Paige Buttrey
# Vigenere Cipher
import random


def generateKey(keySize):
    key = []
    for i in range(keySize):
        key.append(chr(random.randrange(26)+ord('A')))
    #string
    key = "".join(key)
    #generate file
    my_key_file = 'paiges_encryption_key.html'
    #open new file
    key_file_write = open(my_key_file, 'w')
    #write key
    key_file_write.write(key)
    #close file
    key_file_write.close()


    return my_key_file


def encrypt_html(html_data, key):
    #characters that the key skips over
    non_text = ['<','>', '/', '\\', '\n', ' ', '!', ',', '.', '1', '2', '3', '4', '5']
    cipher_text = []
    # for loop visits each line
    for line in html_data:
        # builds new cipher string per line
        cipher_line = ""
        # visit each character in the line
        for characters in range(len(line)):
            # if character is a letter
            if line[characters] not in non_text:
                # if lower case change to upper
                if line[characters].islower():
                    char = line[characters].upper()
                else:
                    char = line[characters]
                x = (ord(char) + ord(key[characters % len(key)])) % 26
                x = x + ord('A')
                cipher_line = cipher_line + chr(x)
            else:
                cipher_line = cipher_line + line[characters]

        cipher_text.append(cipher_line)

    return cipher_text


def decrypt_html(encrypted_data, key):
    non_text = ['<','>', '/', '\\', '\n', ' ', '!', ',', '.', '1', '2', '3', '4', '5']
    original_data = []
    # for loop visits each line
    for line in encrypted_data:
        # builds new cipher string per line
        orig_line = ""
        # visit each character in the line
        for characters in range(len(line)):
            # if character is a letter
            if line[characters] not in non_text:
                char = line[characters]
                x = (ord(char) - ord(key[characters % len(key)]) + 26) % 26
                x = x + ord('A')
                orig_line = orig_line + chr(x)
            else:
                orig_line = orig_line + line[characters]
        original_data.append(orig_line)

    return original_data



def read_html(a_file):
    #open a file to read
    my_file = open(a_file, 'r')
    #read all the tines through
    all_lines = my_file.readlines()
    #close the file
    my_file.close()

    return all_lines

def write_html(data, file_name):
    #open the file to write
    new_file = open(file_name,'w')

    for lines in range(len(data)):
        new_file.write(data[lines])

    new_file.close()


#Create and write key to file
key_size = 8
key_file_name = generateKey(key_size)
encryption_key = read_html(key_file_name)
encryption_key = str(encryption_key)
# read in original html file
original_html_data = read_html("myfile.html")


# encrypt original data
encryption_data = encrypt_html(original_html_data, encryption_key)

# write encrypted data to html file
write_html(encryption_data, 'paiges_encryption_file.html')

# read in encrypted data
encrypted_html_data = read_html('paiges_encryption_file.html')

#decrypted html data
decrypted_html_data = decrypt_html(encrypted_html_data, encryption_key)

# write decrypted data to html file
write_html(decrypted_html_data, 'paiges_decryption_file.html')


#Worked with TA on this code via zoom
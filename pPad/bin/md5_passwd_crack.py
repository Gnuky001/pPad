import hashlib

flag = 0
passwd_hash = raw_input("Enter md5 hashcode: ")
dictionary = raw_input("Dictionary file (leave blank for use default dictionary): ")
passwd_file = ""
if dictionary == "":
    try:
        passwd_file = open("dictionarys/default", "r")
    except:
        print "[!] Error: Couldn't open file!"
        quit()
else:
    try:
        passwd_file = open(dictionary, "r")
    except:
        print "[!] Error: Couldn't open file!"
        quit()

for word in passwd_file:
    print "[*] Trying password: " + word
    encoded_word = word.encode("utf8")
    digest = hashlib.md5(encoded_word.strip()).hexdigest()

    if digest == passwd_hash:
        print "[*] Password found: It is: " + word
        flag = 1
        quit()

if flag == 0:
    print "[!] Password not found!"

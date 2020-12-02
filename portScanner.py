#!/usr/bin/python3

# importing all libraries
import socket
import sys
import threading
# For decoration
usage = "python3 portScanner.py TARGET START_PORT END_PORT"
print("-"*60)
print(" "*10, "PYTHON PORT SCANNER")
print("-"*60)

# checking for the agruments properly typed or not
if(len(sys.argv) != 4):
    print("How to run the tool >> ",usage)
    sys.exit()

#handling the host name & resolve
try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution error")
    sys.exit()

print("SCANNING TARGET ", target, " .....")

start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# created a function for the scanning port using scoket
def pscan(port):
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.settimeout(3)
    conn = s.connect_ex((target, port)) #connect_ex module help not to exit dirctly
    
    if (not conn):
        print("PORT {}  OPEN".format(port))
    s.close()

for port in range(start_port, end_port+1):
    #using thread to manage multiple process 
    thread = threading.Thread(target= pscan, args = (port,))# args contain tuple as single value tuples need comma
    thread.start()    

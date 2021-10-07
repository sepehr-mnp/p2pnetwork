import socket
import os
import json
import hashlib
import inf

myport= inf.port

def hsh(string):
    encoded=string.encode()
    m = hashlib.sha256(encoded)
    return m.hexdigest()[:8]


def send(port,msg):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = '127.0.0.1' #this is ip
        s.settimeout(3)
        s.connect((host,int(port)))
        s.send(msg.encode("utf-8"))
        var=s.recv(1024)
        var=var.decode('utf-8')
        return port,var
        s.close()
    except:
        print("sth went wrong!")
def sendall(msg):
    with open("data_file.json", "r") as my_dictionary:
        data = json.load(my_dictionary)
    returner=[]
    for i in range(len(data)):
        port = int(data["node "+str(i)]["address"])
        returner.append(send(port,msg))
    return returner
def pingpong(port):
    rcvd=send(port,"ping")
    rcvd = rcvd[1]
    if(rcvd == "pong"):
        print("ping_pong completed!")
        
def sendmsg(port,msg):
    try:
        a= int(send(port,str(myport)+"?"+hsh(msg))[1])
        print(a)
        if(a==0):
            send(port,str(myport)+msg)
    except:
        print("sth went wrong")
def sendallmsg(msg):
    with open("data_file.json", "r") as my_dictionary:
        data = json.load(my_dictionary)
    returner=[]
    for i in range(len(data)):
        port = int(data["node "+str(i)]["address"])
        returner.append(sendmsg(port,msg))
    return returner
def fileask(port,filename):
    print(str(myport)+str(myport)+"!"+hsh(filename))
    a= int(send(port,str(myport)+str(myport)+"!"+hsh(filename))[1])
    return a
    
def sendfile(filename,port):
    
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    port= int(port)
    s = socket.socket()
    host = "127.0.0.1"
    s.connect((host, port))
    filesize = os.path.getsize(filename)
    s.send(f"{myport}f{filename}{SEPARATOR}{filesize}".encode())
    #file = open(filename, 'wb') 
    print(s.recv(1024))
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.send(bytes_read)
            #progress.update(len(bytes_read))
    s.close()



    

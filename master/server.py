import socket
import os
from _thread import *
import sender
import friendadder
import messageadder
import inf

ServerSocket = socket.socket()
host = '127.0.0.1'
port = inf.port
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):
    '''
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
    '''
    while True:
        msg = connection.recv(4096)
        if not msg:
            break
        print("s")
        msg = msg.decode()
        print("clint data :",msg[4])
    #check message
                
        
        if msg[0:17]== "wanna be friends?":
            portfriend = int(msg[18:22])
            print(portfriend)
                
            if friendadder.exchecker(portfriend)==1:
                ap=str(friendadder.givenode())
                connection.send(ap.encode("utf-8"))
                print("already exst")
            else:
                ap= "yes"
                connection.send(ap.encode("utf-8"))
                check= sender.send(portfriend,"ping")
                print(check)
                if check[1]== "pong":
                    print("connected!")
                friendadder.add(portfriend)
        elif msg[0:4]=="ping":
            print("hh")
            ap= "pong"
            connection.send(ap.encode("utf-8"))
            #print("connected")
        elif msg[4]=="?":
            print("checking")
            ap= str(messageadder.excheckerhsh(msg[5:],msg[:4]))
            print(ap)
            connection.send(ap.encode("utf-8"))                

        elif msg[8]=="!":
            print(msg)
            ap2 = messageadder.excheckerhsh(messageadder.hsh(msg[9:]),msg[:4])
            ap= messageadder.excheckerhsh2(msg[9:],msg[:4])
            print(ap[0])
            print(ap2)
            connection.send(str(ap[0]).encode("utf-8"))                
            if str(ap2)=="0":
                messageadder.add(msg[9:],msg[:4])
                if (str(ap[0])!="0"):
                    sender.sendfile(ap[1],int(msg[4:8]))
                else:
                    sender.sendall(str(port)+msg[4:])
            else:
                print("already sent!")
        elif msg[4]=="f":
            BUFFER_SIZE = 4096
            SEPARATOR = "<SEPARATOR>"
            sendr = msg[:4]
            msg = msg[5:]
            print("checking")
            ap= str(messageadder.excheckerhsh2(msg[5:],sendr)[0])
            print(ap)
            #print(ap)
            connection.send(ap.encode("utf-8"))                
            
            if ap[0]=="0":
                print("ssS")
                filename, filesize = msg.split(SEPARATOR)
                filename = os.path.basename(filename)
                filesize = int(filesize)
                print(filename+str(filesize))
                messageadder.add2(filename,sendr)
                with open(filename, "wb") as f:
                    while True:
                        bytes_read = connection.recv(BUFFER_SIZE)
                        if not bytes_read:
                            break
                        f.write(bytes_read)    
   
        else:
            print("msg rcvd")
            ap= "rcvd"
            connection.send(ap.encode("utf-8"))
            messageadder.add(msg[4:],msg[:4])
            sender.sendallmsg(msg[4:])
        
    connection.close()
    
while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()


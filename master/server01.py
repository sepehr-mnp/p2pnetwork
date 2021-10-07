import socket
import sender
import friendadder
import messageadder
import inf
while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '' #this is ip
    port = inf.port
    s.bind((host,port))
    s.listen()
    socketclint , address = s.accept()
    print("got conection from :",address)
    msg = socketclint.recv(1024)
    msg = msg.decode("utf-8")
    print("clint data :",msg)
    #check message
    if msg[0:17]== "wanna be friends?":
        portfriend = int(msg[18:22])
        print(portfriend)
            
        if friendadder.exchecker(portfriend)==1:
            ap=str(friendadder.givenode())
            socketclint.send(ap.encode("utf-8"))
            print("already exst")
        else:
            ap= "yes"
            socketclint.send(ap.encode("utf-8"))
            check= sender.send(portfriend,"ping")
            print(check)
            if check[1]== "pong":
                print("connected!")
            friendadder.add(portfriend)
    elif msg[0:4]=="ping":
        print("hh")
        ap= "pong"
        socketclint.send(ap.encode("utf-8"))
        #print("connected")
    elif msg[4]=="?":
        print("checking")
        ap= str(messageadder.excheckerhsh(msg[5:],msg[:4]))
        print(ap)
        socketclint.send(ap.encode("utf-8"))                
        
    else:
        print("msg rcvd")
        ap= "rcvd"
        socketclint.send(ap.encode("utf-8"))
        messageadder.add(msg[4:],msg[:4])
        sender.sendallmsg(msg[4:])
    s.close()
        

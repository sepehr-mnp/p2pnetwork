# p2pnetwork-localEdition
hi dear users!<br>
i guess it was around three months ago that i decided to start building my own blockchain project. so at first i needed a p2p library to connect nodes on my network and send data between them.<br>
but unfortunately there wasnt any projects to automatically build a network from the ground and add nodes to it and the only things that were available, were simle projects that could only connect to nodes manually and could only send one type message to it.<br>
so basically if someone wants to create a blockchain network, not only they should create the blockchain client app itself, but they also have to create the underlying p2p network for message exchaining as well.<br>
thats why i decided to create a project that could help people create a blockchain however they want without having to deal with the zero layer message system. and while building it i asked myself: why should this project only be for blockchain creators? dont other projects like music shairing, video shairing and... need this?
so i changed the code of the project ""so that it can be compatible with any kind of need""!<br>

# !!!important
this version is local host edition, it =s for creating a local p2p simulation in order to test distributed projects,<br>
you might ask, how can p2p network simulator be created on one pc? how many ips does it use? well... the answer is one! only local host(127.0.0.1)! in this version, in contrast of public version that all the nodes use the same port but different ips, nodes use one ip but each of them has a unique port.
 <br>__the one for public network is currently under development, its really easy to edit this one to create that version but i dont have enough pcs and modems to test that version right now so wait or edit the port input with ip yorself__
# how to use
well... i know this early version has some hard things to do and its not completely automatic but im gonna create another script to automatically generate first 3 nodes and create as many as you want. so now that there is no automatic generator, listen(read) carefully:<br>
**1-create first three nodes:** only copy program folder 2 times and then edit port number in *inf.py*(in the image, 5051), use sth in order i suggest and fo rthis version, use 5052 and 5053, its easier to work with.<br>
<img width="100%" src="https://github.com/sepehr-mnp/p2pnetwork/blob/main/p2p01.png"><br>
 but because i love you gus so much, i made it easier for you so you only need to replace the contents form th "put setup" folder with your existing files.<br>
 **2-run nodes:** just click on server.py on each node folder<br>
 **3-add nodes:** -copy the master folder and use edit the *inf.py* script to use another port<br> -then open *finder.py*<br>
the program will at first try to connect to hard coded ports(5051,5052,5053) and after that, it will try to ask them to give a random node port(for the first additional three nodes, program will have near 300 requests! dont worry :) )<bR>
 okay if you add three additional nodes, you will have 6 nodes connected to each other, after that, any node that start will try to connect to 6 nodes and have 2 additional free space for any new nodes that wants to connect to our network.<br>
__!note!__ if you want to check on connected nodes and see if they still working or you should connect to a new node, "run *conexchker.py*."<br>
**okay now you have a network of connected p2p nodes!**
# now create your own program
 
 just edit the *server.py* code and use functions based on your input which is in the *msg*<br>
 <img width="100%" src="https://github.com/sepehr-mnp/p2pnetwork/blob/main/p2p02.png"><br>
 
# useful functions
 - **sender:**<br>
   sender.send(port,message) //sends  message to the port given <br>
   sender.sendall(message)   //sends  message to all the connected nodes<br>
   sender.pingpong(port)     // does a ping pong with the port given<br>
   sender.sendmsg(port,message) //sends  message to the port given but ask them first weather they have the message or not<br>
   sender.sendallmsg(message) //sends  message to all the connected nodes but ask them first weather they have the message or not<br>
   sender.fileask(port,filename) //sends a message to network to ask if anyone has a file with the filename given <br>
   sender.sendfile(filename,port) //sends  message to the port given but ask them first weather they have the message or not<br>
- **messageadder:**<br>
  messageadder.add(message,port) // add message if it doesnt exist already<br>
  messageadder.add2(filename,port) // add file if it doesnt exist already<br>
  messageadder.exchecker(message,port) // checks if the already message exist if it doesnt return 0 if it does return 1 if it does and its from the port given, return 2(this can be used to punish spammer)<br>
    messageadder.exchecker2(filename,port) // checks if a file already exist if it doesnt return 0 if it does return 1 if it does and its from the port given, return 2(this can be used to punish spammer)<br>
  messageadder.excheckerhsh(hsh(message),port) // same as exchecker but checks it by using the last 8 characters of the SHA256 hash of the saved message<br>
  messageadder.excheckerhsh2(hsh(filename),port) // same as exchecker but checks it by using the last 8 characters of the SHA256 hash of the saved filename<br>
 
   

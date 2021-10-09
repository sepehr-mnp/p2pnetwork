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
1- **create first three nodes:** only copy program folder 2 times and then edit port number in *inf.py*, use sth in order i suggest, its easier to work with.


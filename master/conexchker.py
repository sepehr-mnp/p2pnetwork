import time
import sender
import json

with open("data_file.json", "r") as my_dictionary:
    data = json.load(my_dictionary)

    
while True:
    time.sleep(5)
    for i in range(len(data)):
        port = int(data["node "+str(i)]["address"])
        try:
            sender.pingpong(port)
        except:
            print("{0} fucked up!".format(port))
            #del and chk for new node
            

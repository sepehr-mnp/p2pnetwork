import sender
import friendadder
hardcode = [5051,5052,5053]
myport=5054
for s in hardcode:
    i=100
    while i>0:
        try:
            rcvd= sender.send(s,"wanna be friends? {0}".format(str(myport)))
            if rcvd[1]=="yes":
                print("hooray! * {0} wants to be friend with you! :D".format(rcvd[0]))
                friendadder.add(rcvd[0])
                break
            else:
                #inja rcvd haro mirizim to s
                print(rcvd)
                break
            i-=1
        except:
            print("oh no! * {0} doesnt want to be friend with you! he is a bitch! :(".format(s))
            i=0
    
with open("data_file.json", "r") as my_dictionary:
    data = json.load(my_dictionary)
if len(data)<len(hardcode):
    data = hardcode
for p in range(len(data)):
    s = int(data["node "+str(p)]["address"])
    i=100
    while i>0:
        try:
            rcvd= sender.send(s,"wanna be friends? {0}".format(str(myport)))
            if rcvd[1]=="yes":
                print("hooray! * {0} wants to be friend with you! :D".format(rcvd[0]))
                friendadder.add(rcvd[0])
                break
            else:
                #inja rcvd haro mirizim to s
                print(rcvd)
                break
            i-=1
        except:
            print("oh no! * {0} doesnt want to be friend with you! he is a bitch! :(".format(s))
            i=0

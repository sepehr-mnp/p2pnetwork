import json
import hashlib

def hsh(string):
    encoded=string.encode()
    m = hashlib.sha256(encoded)
    return m.hexdigest()[:8]

def add(new_data,new_data_2, filename='messages.json'):
        a = exchecker(new_data,new_data_2)
        hs = hsh(new_data)
        if(a ==2):
                return "fucked up!"
        elif (a==1):
            with open(filename,'r+') as file:
                        file_data = json.load(file)
                        file_data[hs]["recvd"].append(new_data_2)
                        file.seek(0)
                        json.dump(file_data, file)
        else:
                with open(filename,'r+') as file:
                        file_data = json.load(file)
                        y = {hs: {"data":new_data,"recvd":[new_data_2]}}
                        file_data.update(y)
                        file_data["index"].append(hs)
                        file.seek(0)
                        json.dump(file_data, file)

def add2(new_data,new_data_2, filename='messages2.json'):
        a = exchecker2(new_data,new_data_2)
        hs = hsh(new_data)
        if(a ==2):
                return "fucked up!"
        elif (a==1):
            with open(filename,'r+') as file:
                        file_data = json.load(file)
                        file_data[hs]["recvd"].append(new_data_2)
                        file.seek(0)
                        json.dump(file_data, file)
        else:
                with open(filename,'r+') as file:
                        file_data = json.load(file)
                        y = {hs: {"data":new_data,"recvd":[new_data_2]}}
                        file_data.update(y)
                        file_data["index"].append(hs)
                        file.seek(0)
                        json.dump(file_data, file)



def exchecker(newport,newport2):
        a=0
        with open("messages.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        if(hsh(newport) in data):
            a = 1
            if(newport2 in data[hsh(newport)]["recvd"]):
                a = 2
        return a

def exchecker2(newport,newport2):
        a=0
        with open("messages2.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        if(hsh(newport) in data):
            a = 1
            if(newport2 in data[hsh(newport)]["recvd"]):
                a = 2
        return a

def excheckerhsh(newport,newport2):
        a=0
        with open("messages.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        if(newport in data):
            a = 1
            if(newport2 in data[newport]["recvd"]):
                a = 2
            else:
                with open("messages.json",'r+') as file:
                        file_data = json.load(file)
                        file_data[newport]["recvd"].append(newport2)
                        file.seek(0)
                        json.dump(file_data, file)

        return a
def excheckerhsh2(newport,newport2):
        a=0
        filename=""
        with open("messages2.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        if(newport in data):
            a = 1
            filename = data[newport]["data"]
            if(newport2 in data[newport]["recvd"]):
                a = 2
            else:
                with open("messages2.json",'r+') as file:
                        file_data = json.load(file)
                        file_data[newport]["recvd"].append(newport2)
                        file.seek(0)
                        json.dump(file_data, file)

        return a,filename


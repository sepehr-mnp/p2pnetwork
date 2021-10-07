import json
import random
def add(new_data, filename='data_file.json'):
        if(exchecker(new_data)==1):
                return 85# == fucked up
        else:
                with open(filename,'r+') as file:
                        file_data = json.load(file)
                        y = {"node {0}".format(len(file_data)): {"address": new_data, "last ineraction": "", "ban score": 0, "free": True}}
                        file_data.update(y)
                        file.seek(0)
                        json.dump(file_data, file)
         

def exchecker(newport):
        a=0
        with open("data_file.json", "r") as my_dictionary:
            data = json.load(my_dictionary)

        for i in range(len(data)):
                port = int(data["node "+str(i)]["address"])
                if(port ==newport):
                        a=1
        
        return a
def nodecount():
        with open("data_file.json", "r") as my_dictionary:
            data = json.load(my_dictionary)
        return len(data)


def givenode():
        with open("data_file.json", "r") as my_dictionary:
            data = json.load(my_dictionary)
        n = random.randint(0,len(data)-1)
        port = int(data["node "+str(n)]["address"])
        return port


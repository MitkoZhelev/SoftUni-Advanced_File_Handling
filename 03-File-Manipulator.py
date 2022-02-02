import os

def create(name):
    f = open(name,'w')


def add(name,content):
    f = open(name,"a")
    f.write(content+ "\n")

def replace (name,old,new):
    if os.path.exists(name):
        with open(name,'r')as f:
            content = f.read()
        with open(name,'r+') as f:
            content = content.replace(old,new)
            f.write(content)
    else:
        print("An error occurred")

def delete(name):
    if os.path.exists(name):
        os.remove(name)
    else:
        print("An error occurred")


command = input()

while command != "End":
    command = command.split("-")

    if command[0] == "Create":
        create(command[1])
    elif command[0] == "Add":
        add(command[1],command[2])
    elif command[0] == "Replace":
        replace(command[1],command[2],command[3])
    elif command[0] == "Delete":
        delete(command[1])

    command = input()



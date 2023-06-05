import turtle

class Node():
    def __init__(self,data):
        '''This Function establishes the node class'''
        self.data=data
        self.x=0
        self.y=0
        self.connections=[]
        self.node_connections=[]

class Graph():
    def __init__(self,list1):
        """this function establishes the list variable that holds all the nodes, it takes in a list of objects which are not nodes"""
        self.list1=list1
        self.list=[]
        for i in range(len(list1)):#goes through everything in  list1 
            if type(list1[i]) == list:#if its a list then the first value of that list is taken as data and the second one is taken as connections and passed into addnode
                templist=list1[i]
                self.addnode(templist[0],templist[1])
            else:
                self.addnode(list1[i])#passes in only data
        for node3 in self.list:#goes through the lists of connections in each node 
            self.addconnections(node3)
        


    def addnode(self,node,connections=[]):
        '''This function takes in either a node or data and it's connections and adds to self.list and establishes the connections'''
        if type(node) != Node:
            node = Node(node)
        self.list.append(node)
        for t in connections:#goes through the connection list and adds them to the nodes connection list
            if t not in node.connections:
                    node.connections.append(t)
        return node
        

    def addconnections(self,node):
        '''This function goes through a Node objects connections list and sees if there is a node object with that data'''
        for data1 in node.connections:
                for connect_nodes in self.list:
                    if data1 == connect_nodes.data and connect_nodes not in node.node_connections:
                        node.node_connections.append(connect_nodes)

                    
    
    def draw(self):
        global style
        window=turtle.Screen()
        window=turtle.screensize(1000,1000)
        alex = turtle.Turtle()
        alex.shape("turtle")
        alex.speed(0)
        style = ('Courier',20, 'italic')
        alex.penup()
        alex.goto((-250,0))
        length=len(self.list)
        alex.setheading(90)
        for i in range(length):
            pos=alex.pos()
            self.list[i].x=pos[0]
            self.list[i].y=pos[1]
            alex.write(self.list[i].data,font=style)
            alex.right(360/length)
            alex.forward(1000/length)
        for node1 in self.list:
            for connect in node1.node_connections:
                alex.penup()
                alex.goto((node1.x,node1.y))
                alex.pendown()
                alex.goto((connect.x,connect.y))
        alex.hideturtle()
    
    def search(self,input):
        input=str(input)
        for node in self.list:
            if input == node.data:
                r=''
                for f in node.connections:
                    r+=f+', '
                return input+" is connected to "+r
        return False




def textenter():
    input_data=1
    input_list=[]
    while True:
        input_data=input("What data would you like to add? ")
        if input_data == "No More Data":
            break
        input_connections=input("Please list, seperated by commas, what this data is connected to? ")
        input_connections=input_connections.split(',')
        input_list.append([input_data,input_connections])
    return Graph(input_list)

def read_enter(document):
    input_list=[]
    with open(document,'r') as myfile:
        text=myfile.readlines()
        for line in text:
            line=line.split(',')
            line[-1]=line[-1].strip("\n")
            input_data=line[0]
            input_connections=line[1:]
            input_list.append([input_data, input_connections])
    return Graph(input_list)

graph=read_enter("text.txt")
graph.draw()
input()





'''
Traditional Stack Implementation

Author : C.Manikandan

'''
import operator 

class  Stack():
    def __init__(self):
        self.items =[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        self.items.pop()
    def isEmpty(self):
        return (self.items == [])


if __name__ == "__main__":
    myObj = Stack()
    print myObj.isEmpty()
    myObj.push("mani")
    myObj.push("sani")
    myObj.push("john")
    print myObj.isEmpty()

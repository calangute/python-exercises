class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def isEmpty(self):
        return self.items == []

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)



def hotPotato(namelist, num):
    simq = Queue()
    for name in namelist:
        simq.enqueue(name)

    while simq.size()>1:
        for i in range(num):
            simq.enqueue(simq.dequeue())
        simq.dequeue()

    return simq.dequeue()


print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],7))



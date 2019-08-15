from random import randrange


def flip():
    return randrange(2)


class HeaderNode:
    def __init__(self):
        self.next = None
        self.down = None

    def getNext(self):
        return self.next

    def getDown(self):
        return self.down

    def setNext(self, newnext):
        self.next = newnext

    def setDown(self, newdown):
        self.down = newdown


class DataNode:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.next = None
        self.down = None

    def getKey(self):
        return self.key

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getDown(self):
        return self.down

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setDown(self, newdown):
        self.down = newdown


class SkipList:
    def __init__(self):
        self.head = None

    def search(self, key):
        current = self.head
        found = False
        stop = False
        while not found and not stop:
            if current is None:
                stop = True
            else:
                if current.getNext() is None:
                    current = current.getDown()
                else:
                    if current.getNext().getKey() == key:
                        found = True
                    else:
                        if key < current.getNext().getKey():
                            current = current.getDown()
                        else:
                            current = current.getNext()
        if found:
            return current.getNext().getData()
        else:
            return None

    def insert(self, key, data):
        if self.head is None:
            self.head = HeaderNode()
            temp = DataNode(key, data)
            self.head.setNext(temp)
            top = temp
            while flip() == 1:
                newhead = HeaderNode()
                temp = DataNode(key, data)
                temp.setDown(top)
                newhead.setNext(temp)
                newhead.setDown(self.head)
                self.head = newhead
                top = temp
        else:
            towerStack = Stack()
            current = self.head
            stop = False
            while not stop:
                if current is None:
                    stop = True
                else:
                    if current.getNext() is None:
                        towerStack.push(current)
                        current = current.getDown()
                    else:
                        if current.getNext().getKey() > key:
                            towerStack.push(current)
                            current = current.getDown()
                        else:
                            current = current.getNext()

            lowestLevel = towerStack.pop()
            temp = DataNode(key, data)
            temp.setNext(lowestLevel.getNext())
            lowestLevel.setNext(temp)
            top = temp
            while flip() == 1:
                if towerStack.isEmpty():
                    newhead = HeaderNode()
                    temp = DataNode(key, data)
                    temp.setDown(top)
                    newhead.setNext(temp)
                    newhead.setDown(self.head)
                    self.head = newhead
                    top = temp
                else:
                    nextLevel = towerStack.pop()
                    temp = DataNode(key, data)
                    temp.setDown(top)
                    temp.setNext(nextLevel.getNext())
                    nextLevel.setNext(temp)
                    top = temp


class Map:
    def __init__(self):
        self.collection = SkipList()

    def put(self, key, value):
        self.collection.insert(key, value)

    def get(self, key):
        return self.collection.search(key)

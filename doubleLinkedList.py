class linkedList:
    def __init__(self):
        self.first = None
        self.last = None
    def insertEnd(self, data):
        n = node(data)
        if not self.first:
            self.first = n
            self.last = n
            return 0
        n.previous = self.last
        self.last.next = n
        self.last = n
    def saveList(self):
        s = ""
        currentNode = self.first
        while currentNode:
            s += str(currentNode.data) + " "
            currentNode = currentNode.next
        s += "\n"
        return s
import node


class DoubleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def insert_end(self, data):
        n = node.Node(data)
        if not self.first:
            self.first = n
            self.last = n
            return 0
        n.previous = self.last
        self.last.next = n
        self.last = n

    def save_list(self):
        s = ""
        current_node = self.first
        while current_node:
            s += str(current_node.data) + " "
            current_node = current_node.next
        s += "\n"
        return s

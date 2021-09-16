class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.ssize = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None
        
    def nodeAt(self, index):
        if index >= -1:
            if index > self.size()-1:
                index = self.size()-1
            p = self.head               # Dummy head
            for _ in range(-1, index):
                p = p.next
            return p        # return Node
        else:
            if index < -self.size()-1:
                index = -self.size()-1
            index = -index-1
            p = self.tail               # Dummy Tail
            for _ in range(-1, index):
                p = p.prev
            return p        # return Node
    def append(self, item):
        self.insert(self.size(), item)

    def addHead(self, item):
       self.insert(0, item)

    def insert(self, pos, item):
       prevNode = self.nodeAt(pos-1)  
       newNode = Node(item, prevNode, prevNode.next)
       prevNode.next = newNode.next.prev = newNode

    def search(self, item):
         p = self.head.next
         while p is not None:
            if p.data == data:
                return 'Found'
            p = p.next
         return 'Not Found'

    def index(self, item):
        p = self.head.next
        for i in range(self.size()):
            if p.data == data:
                return i
            p = p.next
        return -1

    def size(self):
        return self.ssize

    def pop(self, pos):
        if not 0 <= index < self.size():
            return 'Out of Range'
        # store node
        currentNode = self.nodeAt(index-1).next

        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev

        self.ssize -= 1
        return 'Success'

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
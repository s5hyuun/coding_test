class DNode:
    def __init__(self, elem, prev=None, next = None):
        self.data = elem
        self.next = next
        self.prev = prev

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
        self.next = node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
    
class DblLinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def isFull(self):
        return False
    
    def clear(self):
        self.head = None

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.next
            count += 1
        return count
    
    def display(self, msg='DblLinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end='<=>')
            ptr = ptr.next
        print('None')

    def getNode(self, pos):
        if pos < 0: 
            return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
        
    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None:
            node.data = elem
    
    def find(self, val):
        node = self.head
        while node is not None:
            if node.data == val:
                return node
            node = node.next
        return node
    
    def insert(self, pos, elem):
        node = DNode(elem)
        before = self.getNode(pos-1)
        if before == None:
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self.head = node
        else:
            before.append(node)

    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.next
                self.head.prev = None
        else:
            before.popNext()

s = DblLinkedList()
s.display('연결리스트(초기): ')
s.insert(0, 10)
s.insert(0, 20)
s.insert(1, 30)
s.insert(s.size(), 40)
s.insert(2, 50)
s.display('연결리스트(삽입x5): ')
s.replace(2, 90)
s.display('연결리스트(교체x1): ')
s.delete(2)
s.delete(3)
s.delete(0)
s.display('연결리스트(삭제x3): ')

l = []
print('파이썬list(초기): ', l)
l.insert(0, 10)
l.insert(0, 20)
l.insert(1, 30)
l.insert(len(l), 40)
l.insert(2, 50)
print('파이썬list(삽입x5): ', l)
l[2] = 90
print('파이썬list(교체x1): ', l)
l.pop(2)
l.pop(3)
l.pop(0)
print('파이썬list(삭제x3): ', l)
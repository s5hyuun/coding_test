class ArrayQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else : 
            pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: 
            pass

    def peek(self):
        if not self.isEmpty():
            if not self.isEmpty():
                return self.array[(self.front + 1) % self.capacity]
            else:
                pass
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, msg='Queue:'):
        print(msg, end='= [')
        count = self.size()
        for i in range(count):
            print(self.array[(self.front + 1 + i) % self.capacity], end= '')
        print("]")

    # 링 버퍼를 위한 삽입 연산 >> 추가된 코드         
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front = (self.front + 1) % self.capacity

import random
if __name__ == "__main__":
    q = ArrayQueue(8)

    q.display("초기 상태")
    for i in range(6):
        q.enqueue2(i)
    q.display("삽입 0-5")

    q.enqueue2(6); q.enqueue2(7)
    q.display("삽입 6, 7")

    q.enqueue2(8); q.enqueue2(9)
    q.display("삽입 8, 9")

    q.enqueue(); q.enqueue()
    q.display("삭제 x2")

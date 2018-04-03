class Queue:

    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue==[]

    def enque(self,data):
        self.queue.append(data)

    def deque(self):
        data=self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        if len(self.queue)==0:
            return False
        else:
            return self.queue[0]


    def size(self):
        return len(self.queue)

queue=Queue()
queue.enque(200)
queue.enque(99)
print(queue.deque())
print(queue.peek())
print(queue.deque())
print(queue.size())
print(queue.peek())

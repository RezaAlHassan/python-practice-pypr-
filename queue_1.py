
class Queue():
    def __init__(self):
        self.queue = []


    def isempty(self):
        return not len(self.queue)

    def enqueue(self, element):
        self.queue.append(element)
        


    def dequeue(self):
        if self.isempty():
            return "Warning: The queue is empty"
        self.queue.pop(0)

    
    def peek(self):
        if self.isempty():
            return "Warning: The queue is empty"
        return self.queue[0]

#Optional/Extra function. Just only for display. No use for queue functionality
    def printQueue(self):
       if self.isempty():
        print("Queue is empty")
       else:
        print(self.queue)  
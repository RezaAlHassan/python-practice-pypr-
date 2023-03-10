
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

class Stack:
    def __init__(self):
        self.__data = []
        
    def size(self):
        return len(self.__data)
    
    def isempty(self):
      if self.size()==0:
        return True
      else: 
        return False  
    
    # Push data to the top of the stack
    def push(self, data):
        self.__data.append(data)
        
    def pop(self):
      if self.isempty():
        print("Stack is empty")
      else:
         self.__data.pop() 
       
    

    def peek(self):
      if self.isempty():
        print("Stack is empty")
      else:
        return self.__data[-1]  
    def clearTahmid(self):
       if self.isempty():
        print("Stack is empty")
       else:
        self.__data.clear() 

#Optional/Extra function. Just only for display. No use for stack functionality
    def printStack(self):
       if self.isempty():
        print("Stack is empty")
       else:
        print(self.__data)  

  #delete a number less than the given from the stack. a queue must can be used  
    def deleteX(self,val):
       q=Queue()
       #for i in range(self.size()-1,-1,-1):
       for i in range(self.size()):
            if self.__data[i]>val:
                q.enqueue(self.__data[i])
       q.printQueue()
    

s=Stack()
s.push(3)
s.push(5)
s.push(7)
s.push(1)
s.deleteX(4)

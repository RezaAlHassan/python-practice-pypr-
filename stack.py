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


def reverseString(str):
        s = Stack()
        for ch in str:
            s.push(ch)
  
        rev = ""
        for i in range (0, s.size()):
            ch = s.peek()
            rev += ch
            s.pop()
        return rev

        print(reverseString("WATERMELON"))
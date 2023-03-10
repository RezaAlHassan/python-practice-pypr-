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


#checks the ordering of brackets in a stack/list
def checkBrackets(self):
    brackets_open = ["(", "[", "{"]
    brackets_close = [")", "]", "}"]
    stack = Stack()

    for bracket in self.__data:
        if bracket in brackets_open:
            stack.push(bracket)
        elif bracket in brackets_close:
            if stack.isEmpty():
                return False
            if brackets_close.index(bracket) != brackets_open.index(stack.pop()):
                return False
    return stack.isEmpty()

  #maintaining ascending order
def pushStack(self, value):
      if self.isEmpty():
        self.push(value)
      else:
        temp_stack = Stack()
        while (not self.isEmpty()) and self.peek() < value:
            temp_stack.push(self.pop())
        self.push(value)
        while not temp_stack.isEmpty():
            self.push(temp_stack.pop())

def LargestOnTop(self):
        stack=Stack()
        if self.isempty():
           print("Stack is empty")
        else:
            max=self.peek()
            for i in self.__data:
                if max<i:
                    max=i
            for i in self.__data:
                if(i != max):
                    stack.push(i)
            stack.push(max)
            return stack
        
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
      

def textEditor(self):
        print('Press 1 to enter string and 2 to delete string')
        f=int(input())
        if f==1:
            print('how many words do you want to enter?')
            wordcnt=int(input())
            for i in range(wordcnt):
                string=input()
                self.push(string)
        elif f==2:
            if self.isempty():
                print('stack empty')
            else:
                self.pop()
        print(self.__data)
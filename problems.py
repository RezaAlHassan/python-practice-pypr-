#Given a string of brackets, determine whether each sequence of brackets is balanced
def bracketCheck(brackets):
  stack = []
  for bracket in brackets:
    if bracket == '[' or bracket == '{' or bracket == '(':
      stack.append(bracket)
    elif bracket == ']':
      if len(stack) == 0 or stack.pop() != '[':
        return False
    elif bracket == '}':
      if len(stack) == 0 or stack.pop() != '{':
        return False
    elif bracket == ')':
      if len(stack) == 0 or stack.pop() != '(':
        return False
  return len(stack) == 0


def keepLargestOnTop(stack):
  max=stack[0]
  for num in stack:
    if max<num:
      max = num
  stack.append(max)
  stack.remove(max)
  return stack

def keepLargestOnTop(stack):
  max=stack[0]
  for num in stack:
    if max<num:
      max = num
  stack.append(max)
  stack.remove(max)
  return stack

def balanceSumInStacks(stack1,stack2):
  sum1=0
  sum2=0
  for num in stack1:
    sum1=sum1+num
  for num in stack2:
    sum2=sum2+num 
  
  if sum1>sum2:
     diff=sum1-sum2
     stack2.append(diff)
     return stack1
  elif sum1<sum2:
     diff=sum2-sum1
     stack1.append(diff)
     return stack2
  

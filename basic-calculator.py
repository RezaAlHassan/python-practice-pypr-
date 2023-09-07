
def add(a,b):
 # return print(a+b) dont do this, its safer to:
   return a+b
 
def sub(a,b):
  return b-a
  
def multiply(a,b):
  return a*b
  
def div(a,b):
  if b!=0:
        return a/b
  else:
        return "Error: Division by zero"
  
def main():
    print('first number:')
    a=float(input())
    print('second number:')
    b=float(input())
    print('press 1 to add, press 2 to subtract, press 3 to multiply,press 4 to divide ')
    f=int(input())
    if f==1 :
      r= add(a,b)
      print('the result is' + " " + str(r))
    elif f==2 :
       sub(a,b)
    elif f==3 :
       multiply(a,b)
    elif f==4 :
       div(a,b)
    else:
       print('Invalid input')   #if divided by 0
main()

# When you use if for each condition, each if statement is evaluated independently, regardless of whether the previous conditions were true or false. This means that if you use if for all conditions, all of them will be checked one after the other, even if one of them is true. This can lead to multiple conditions being true, and all corresponding code blocks executing.
# elif is used to test multiple conditions in a sequential manner. When you use elif, the conditions are evaluated one by one, and as soon as a true condition is encountered, its corresponding code block is executed, and the rest of the conditions are skipped.
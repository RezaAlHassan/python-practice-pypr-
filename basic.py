#print triangle
def printTriange(c, n):
    myList = []
    for i in range(0, n):
        myList.append("*"*i)
    print("\n".join(myList))

#find sphere volume
def findVolume(r):
    v=2*3.14*(r**3)
    return v

def findFactorial(n):
    fact=1
    while(n>0):
        fact=fact*n
        n=n-1
    return fact

#find no of digits in an integer
def noOfDigits(n):
    f=len(str(n))
    return f

#find sum of digits in an integer
def sumOfDigits(n):
    sumD=0
    while n>0:
        rem=n%10
        n=n//10 #floor division
        sumD=sumD+rem
    return sumD  

#reverse digits in an integer
def reverseDigits(n):
    sumD=""
    while n>0:
        rem=str(n%10)
        n=n//10 #floor division
        sumD=sumD+rem
    return int(sumD) 

def findHcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf

def findLcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

def checkPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
        return True
def checkPerfect(n):
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")
def checkPalindrome(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")

def minmaxavg(arr):
    maxr=arr[0]
    minr=arr[0]
    sumr=arr[0]
    for i in arr:
        if maxr<i:
            maxr=i
        if minr>i:
            minr=i
        sumr=sumr+i
        
    avg=sumr/len(arr)
    return maxr,minr,avg

#with loop
def noOfwordss(s):
    count=0
    for i in s:
        if i==" ":
            count=count+1
    return count
#without loop
def noOfletters(s):
    f=s.split(" ")
    words=len(f)
    return words

def toUpper(s):
    return s.upper()

def checkID(s):
    check=False
    if(len(s)<5):
        return check
    else:
        year=int(s[0]+s[1])
        month=int(s[2]+s[3])
        for i in range(0,len(s)-1):
            if (year in range (00,23)) and (month in range (00,13)):
                check=True
        return check

def theAns():
    print('the answer to life, the universe and everything')

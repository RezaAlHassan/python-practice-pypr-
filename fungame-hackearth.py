#https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/fun-game-91510e9f/?purpose=login&source=problem-page&update=google
n = int(input())               
newlst=[]
lst = list(map(int, input().strip().split()))[:n]
f=len(lst)-1
for i in range(0,(len(lst)-1)):
    if len(lst)==1:
        newlst.append(0)
        
    elif lst[0]>lst[-1]:
        lst.pop(-1)
        newlst.append(1)
        
    elif lst[0]<lst[-1]:
        lst.pop(-1)
        f=len(lst)-1
        newlst.append(2)
        
    elif lst[0]==lst[-1]:
        newlst.append(0)
        lst.pop(0)
        lst.pop(-1)
     
        #f=len(lst)-1
        
print(newlst)

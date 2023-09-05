#John and Barry are brothers. Their dads age is one and half time their age summed together. 
#What is their dads age?
import math

print('Enter John age:')
ageJohn=int(input()) #converting to int because input taken as string
print('Enter Barry age:')
ageBarry=int(input())
dadAge=1.5*(ageJohn+ageBarry)
#print('ageDad:' + dadAge) will show error because only stribgs can be concactenated

print('ageDad:', dadAge) #will show float number.age cannot be float so:
print('ageDad:', math.floor(dadAge)) #to use floor function import math library
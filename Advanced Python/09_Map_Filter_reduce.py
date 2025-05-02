from functools import reduce
#Map Function

l = [1,2,3,4,5,6]
square=lambda x:x*x
sqList=map(square,l)
print(list(sqList))

#Filter Function 
def Even(n):
    if(n%2==0):
        return True
    return False
def Odd(n):
    if(n%2==1):
        return True
    return False

onlyEven=filter(Even,l)
print(list(onlyEven))

onlyODD=filter(Odd,l)
print(list(onlyODD))

#Reduce Function
def sum(a,b):
    return a+b
mul = lambda x,y:x*y

print(reduce(sum,l))
print(reduce(mul,l))
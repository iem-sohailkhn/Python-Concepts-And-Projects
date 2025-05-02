def Divisible5(n):
    if(n%5==0):
        return True
    return False
s = [1,2,5,10,33,35,66,55,77,60]
f = list(filter(Divisible5,s))
print(f)
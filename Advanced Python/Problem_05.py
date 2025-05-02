from functools import reduce
l = [1,11,2,222,333,444,555]
def MAximum(a,b):
    if(a>b):
        return a
    return b
print(reduce(MAximum,l))

    
    
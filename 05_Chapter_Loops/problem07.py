n= int(input("Enter Number..."))

for i in range(n,0,-1):
    # print(" "* (n-i),end="")
    # print("*"* (2*i-1),end="")
    print(" " * (n-i),end="")
    print("*" * (2*i-1))
    # print("")
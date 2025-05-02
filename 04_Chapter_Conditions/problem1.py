#Greatest Of Four Numbers
a=int(input("Enter Number 1..."))
b=int(input("Enter Number 2..."))
c=int(input("Enter Number 3..."))
d=int(input("Enter Number 4..."))

if(a>b and a>c and a>d):
    print(f"{a} is Greatest")

elif(b>a and b>c and b>d):
    print(f"{b} is Greatest")
elif(c>a and c>b and c>d):
    print(f"{c} Is Greatest")
else:
    print(f"{d} is Greatest..")

print("End Of Program...")


a= int(input("Enter a number..."))
b = int(input("Enter sec number..."))

if(b==0):
    raise ZeroDivisionError("Alert!!!!! Denomenator Can't be zero ")

else:
    print(f"The division of a/b is {a/b}")


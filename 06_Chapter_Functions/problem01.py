def Greatest_Of_Number(a,b,c):
    # a = int(input("Enter A Number..."))
    # b = int(input("Enter A Number..."))
    # c = int(input("Enter A Number..."))

    if(a>b and a>c):
        print(f"{a} is Greatest")
    elif(b>a and b>c):
        print(f"{b} Is greatest ")
        
    else:
        print(f"{c} is Greatest")

Greatest_Of_Number(3,4,5)
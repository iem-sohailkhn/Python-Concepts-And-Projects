SE=int(input("Enter SE Marks..."))
DB=int(input("Enter SE Marks..."))
CN=int(input("Enter SE Marks..."))
marks1=(SE/100)*100
marks2=(DB/100)*100
marks3=(CN/100)*100
marks=((SE+DB+CN)/100)*100
if(marks1>33 and marks2>33 and marks3>33 and marks>40):
    print(f"You have Passed  Congratulations with {marks}")
else:
    print("Sorry Try Again ..You Failed")
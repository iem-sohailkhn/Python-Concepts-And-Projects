'''
1 for Snake
-1 for water
0 for gun
'''
import random
computer =random.choice([1, -1, 0])
youstr=input("Enter Yours Choice: ")
youDict={"s":1,"w":-1,"g":0}
you = youDict[youstr]

if(computer==you):
    print(f"Computer Choose {computer}\n You Choose {you}\nIts A Draw")

else:
    if(computer==-1 and you==1):
        print(f"Computer choose{computer}\n You choose {you} \nYou win!")
    
    elif(computer==-1 and you==0):
        print(f"Computer Choose {computer}\n You Choose {you}\n You Lose!")
    elif(computer==1 and you==-1):
        print(f"Computer Choose {computer}\n You Choose {you}\n You lose!")
    elif(computer==1 and you==0):
        print(f"Computer Choose {computer}\n You Choose {you}\n You win!")
    elif(computer==0 and you==-1):
        print(f"Computer Choose {computer}\n You Choose {you}\n You win!")
    elif(computer==0 and you==1):
        print(f"Computer Choose {computer}\n You Choose {you}\n You lose!")
    else:
        print("Something Went Wrong......")
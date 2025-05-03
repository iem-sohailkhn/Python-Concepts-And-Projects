'''
Initialize input other than 1 to 100
while condition random no != input
if a>n
print
else a<n
print
'''
import random
n = random.randint(1,100)
a=-1
guess=1
while (a!=n):
    try:
        a=int(input("Enter number between 1 to 100.."))
        if(a<1 or a>100):
            print("Please enter number between 1  to 100..")
        if(a>n):
            print("Please enter lower number...")
        elif(a<n):
            print("Please enter higher number...")
        guess+=1
    except ValueError:
        print("Invalid Option..")
print(f"You guess the number {n} correctly in {guess} guesses")


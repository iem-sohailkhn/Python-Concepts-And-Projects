import random
n = random.randint(1,100)
a=-1#  The value of a should be other than 1,100
guesses=1
while (a!=n):

    a = int(input("Enter a number please...."))
    if(a>n):
        print("Please enter lower number...")

    elif(a<n):
        print("Please enter Higher number...")
    guesses+=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")



'''
Take input from user as yess or no if they want to play 
if yes then enter in the loop 
take number of dice they want to
generate /rolled the dice number of dice times
print rolled/generated 
else if no 
thanks for playing
else 
invalid number
'''
import random

count = 0
while True:
    choice = input("You want to roll the dice (y/n): ")
    if(choice.lower()=="y"):
        try:
            num_dice=int(input("How many times do you want to roll the dice: "))
            if(num_dice<0):
              print("Please enter number greater than 0: ")
              continue
        except ValueError:
            print("Invalid number. please enter greater than 0..")

        count+=1
        print(f"Rolling the {num_dice} dice(s)")

        for i in range(1,num_dice+1):
            rolled = random.randint(1,6)
            print(f"Number {i} rolled is {rolled}")

        print(f"You have rolled the dice {count} times")
    elif(choice.lower()=="n"):
        print("Thanks for playing the game.")
        break
    else:
        print("Invalid option.choose y/n..")

        



# Number gussing Game
'''In this game you guss a Number and If you guss correct number the you win
Hint 1: If you put large Number then You found Message "Too High"
Hint 2: If you put large Number then You found Message "Too Low" 
'''
import random

Warning_number=random.randint(1,100)
user_input=int(input("Guss a number from 1 to 100 : "))

i=0
while True:
    
    if Warning_number==user_input:
        print(f'You Win:  And you Gassed this number in {i} times')
        break

    elif Warning_number >user_input:
        print("Too Low:")
        i+=1
        user_input=int(input("Guss again : "))
        continue

    else :
        print("Too High:")
        i+=1
        user_input=int(input("Guss again : "))
        continue
print("\n\n\U0001F497  Welcom to Next level: \U0001F497\n\n")


Warning_number=random.randint(1,200)
user_input=int(input("Guss a number from 1 to 200 : "))

i=0
while True:
    
    if Warning_number==user_input:
        print(f'You Win:  And you Gassed this number in {i} times')
        break

    elif Warning_number >user_input:
        print("Too Low:")
        i+=1
        user_input=int(input("Guss again : "))
        continue

    else :
        print("Too High:")
        i+=1
        user_input=int(input("Guss again : "))
        continue
print("\n\n\U0001F497  Welcom to Next level: \U0001F497\n\n")
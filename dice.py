import random

while True:
    print('''
1. Roll the dice
2. Exit''')
    user_enter = int(input("What do you want?: "))
    if user_enter == 1:
        number = random.randint(1,6)
        print(f"The number is {number}.")
    elif user_enter == 2:
        break
    else: 
        print("Invalid input...Please enter 1 or 2")
    
    
    
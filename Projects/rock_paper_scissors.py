import random
import os
import subprocess
GameLoop = True
user_input = 'null'
user_choice = 'null'
cpu_choice = 'null'

while True:
    print("1. Rock\n2. Paper\n3. Scissors")
    user_input = input()
    user_input = int(user_input)
    if user_input > 3 or user_input < 1:
        print("Please Enter a Valid Option!")
    break
os.system('clear')
if user_input == 1:
    user_choice = 'Rock'
    print("User Choice: " + user_choice)
elif user_input == 2:
    user_choice = "Paper"
    print("User Choice: " + user_choice)
else:
    user_choice = "Scissors"
    print("User Choice: " + user_choice)

cpu = random.randint(1, 3)
if cpu == 1:
    cpu_choice = "Rock"
    print("Computer Choice: " + cpu_choice)
elif cpu == 2:
    cpu_choice = "Paper"
    print("Computer Choice: " + cpu_choice)
else:
    cpu_choice = "Scissors"
    print("Computer Choice: " + cpu_choice)

if user_choice == "Rock" and cpu_choice == "Rock":
    print("Tie Game")
elif user_choice == "Paper" and cpu_choice == "Paper":
    print("Tie Game")
elif user_choice == "Scissors" and cpu_choice == "Scissors":
    print("Tie Game")
elif user_choice == "Rock" and cpu_choice == "Paper":
    print("Paper beats Rock!\nCPU wins!")
elif user_choice == "Scissors" and cpu_choice == "Paper":
    print("Scissors beats Paper!\nUser wins!")
elif user_choice == "Paper" and cpu_choice == "Rock":
    print("Paper beats Rock!\nUser wins!")
elif cpu_choice == "Rock" and user_choice == "Scissors":
    print("Rock beats Scissors!\nCPU wins!")
elif cpu_choice == "Scissors" and user_choice == "Paper":
    print("Scissors beats Paper!\nCPU wins!")
elif cpu_choice == "Scissors" and user_choice == "Rock":
    print("Rock beats Scissors!\nUser wins!")

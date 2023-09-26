import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
choicesList = [rock, paper, scissors]

if choice == 0:
    print(choicesList[choice])
    cpuChose = choicesList[random.randint(0, 2)]
    print(f"Computer chose:\n{cpuChose}")
    if cpuChose == choicesList[2]:
        print("You win!")
    elif cpuChose == choicesList[0]:
        print("It's a draw!")
    else:
        print("You lose")
elif choice == 1:
    print(choicesList[choice])
    cpuChose = choicesList[random.randint(0, 2)]
    print(f"Computer chose:\n{cpuChose}")
    if cpuChose == choicesList[0]:
        print("You win!")
    elif cpuChose == choicesList[1]:
        print("It's a draw!")
    else:
        print("You lose")
elif choice == 2:
    print(choicesList[choice])
    cpuChose = choicesList[random.randint(0, 2)]
    print(f"Computer chose:\n{cpuChose}")
    if cpuChose == choicesList[1]:
        print("You win!")
    elif cpuChose == choicesList[2]:
        print("It's a draw!")
    else:
        print("You lose")
else:
    print("Wrong Input!")

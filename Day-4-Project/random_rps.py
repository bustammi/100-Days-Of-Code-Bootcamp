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

#Write your code below this line 👇
choice = [rock, paper, scissors]
user_selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
randomAI_selection = random.randint(0, len(choice) - 1)



if user_selection == "0":
    print("You chose: \n")
    print(rock)
    print("Computer chose: \n")
    randomAI_choice = str(choice[randomAI_selection])
    print(randomAI_choice)
    if randomAI_choice == choice[0]:
        print("It's a draw!")
    elif randomAI_choice == choice[1]:
        print("You lose!")
    else:
        print("You win!")

elif user_selection == "1":
    print("You chose: \n")
    print(paper)
    print("Computer chose: \n")
    randomAI_choice2 = str(choice[randomAI_selection])
    print(randomAI_choice2)
    if randomAI_choice2 == choice[0]:
         print("You win!")
    elif randomAI_choice2 == choice[1]:
        print("It's a tie!")
    else:
        print("You lose")
    
else:
    print("You chose: \n")
    print(scissors)
    print("Computer chose: \n")
    randomAI_choice3 = str(choice[randomAI_selection])
    print(randomAI_choice3)
    if randomAI_choice3 == choice[0]:
         print("You lose!")
    elif randomAI_choice3 == choice[1]:
        print("You win!")
    else:
        print("It's a tie!")
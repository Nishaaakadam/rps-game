import random 

user_input = input("Enter your choice (rock,paper,scissors)")
possible_choices = ["rock","paper","scissors"]
computer_input = random.choices(possible_choices)

print(f"You choose{user_input},computer choose {computer_input}")


if user_input == computer_input:
    print(f"Its a Draw as both selected {user_input}")
elif user_input == "rock":
    if computer_input == "scissors":
        print("user wins,Rock will break the scissors")
    else:
        print("user lose, paper will cover rock")
elif user_input == "paper":
    if computer_input == "rock":
        print("user wins, paper will cover rock")
    else:
        print("user lose, scissors will cut the paper")

elif user_input == "scissors":
    if computer_input == "paper":
        print("user wins, scissors will cut the paper")
    else:
        print("user lose, Rock will break the scissors")


                
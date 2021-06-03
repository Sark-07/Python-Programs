import random

print("Rock Paper scissor Game ")
print("You have 5 chances")
lis = ["rock", "paper", "scissor"]
i = 0
point_user = 0
point_computer = 0
while i < 5:
    user = input("Enter your choice: ")
    user1 = user.lower()
    a = random.choice(lis)
    if user1 == "rock" and a == "paper":
        point_computer += 1
        print("You chose rock and computer chose paper so, computer wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == "paper" and a == "rock":
        point_user += 1
        print("You chose paper and computer chose rock so, you wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == "rock" and a == "scissor":
        point_user += 1
        print("You chose rock and computer chose scissor so, you wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == "scissor" and a == "rock":
        point_computer += 1
        print("You chose scissor and computer chose rock so, computer wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == "paper" and a == "scissor":
        point_computer += 1
        print("You chose paper and computer chose scissor so, computer wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == "scissor" and a == "paper":
        point_user += 1
        print("You chose scissor and computer chose paper so, computer wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    elif user1 == a:
        print("It's tie!")
        point_user += 0
        point_computer += 0
        print(f"You chose {user1} and computer also chose {a} so, no one wins")
        print(f"Your point = {point_user} and computer's point = {point_computer}")
        i += 1
    else:
        print("You have entered wrong input!!")
        i += 0

if point_user > point_computer:
    print(f"You win!! Your point is = {point_user} and computer's point is = {point_computer}")
elif point_user < point_computer:
    print(f"You loose!! Your point is = {point_user} and computer's point is = {point_computer}")
else:
    print("It's a tie!! No one wins!")

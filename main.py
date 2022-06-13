# winning rules
# rock beats paper
# paper beats rock
# scissors beats paper
import random
print("winning rules of the rock, paper, scissors game:\n"+ "rock vs paper => paper wins \n" + "rock vs scissors => rocks wins \n" + "paper vs scissors => scissors wins \n" )
while True:
    print("Enter choice \n 1 for rock \n 2 for paper \n 3 for scissors \n")
    choice = int(input("enter a valid input: "))

    if choice == 1:
        choice_name = "rock"
    elif choice == 2:
        choice_name = "paper"
    else:
        choice_name = "scissors"
    print("user choice is: " + choice_name)
    print("\nNow its computer's turn......")

    computer_choice = random.randint(1,3)
    while computer_choice == choice:
        computer_choice = random.randint(1,3)
    
    if computer_choice == 1:
        computer_choice_name = "rock"
    elif computer_choice == 2:
        computer_choice_name = "paper"
    else: computer_choice_name = "scissors"

    print("computer choice is: " + computer_choice_name)
    print (choice_name + " vs " + computer_choice_name)
    if ((choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1)):
        print("paper wins => ", end = "")
        result = "paper"

    elif ((choice == 1 and computer_choice == 3) or (choice == 3 and computer_choice == 1)):
        print("rock wins =>", end = "")
        result = "rock"
    else:
        print("scissors wins =>", end =  "")
        result = "scissors"
    if result ==  choice_name:
        print("<== user wins ==>")
    else :
        print("<== computer wins ==>")

    print("do you want to play again? (Y/N)")
    ans = input()

    if ans == "n" or ans == "N":
        print("\nThanks for playing")
        break

   



    




    
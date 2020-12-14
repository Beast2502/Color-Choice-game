import random

print("Winning ules of the Color choice Game as follows: " + "\nEnter a number from one two five and match computer choice to win the computer.")

computer_score = 0
player_score = 0 


while True:
    print("red = 1 \nyellow = 2 \norange = 3 \ngreen = 4 \nblue = 5 \ntake a turn :")

    #take the input from the user

    player_choice = int(input("User turn: "))

    while player_choice > 5 and player_choice <1:
        player_choice = int(input("enter the valid input : "))
        
    if player_choice  ==1:
        choice_col = 'red'
    elif player_choice ==2:
        choice_col = 'yellow'
    elif player_choice == 3:
        choice_col='orange'
    elif player_choice == 4:
        choice_col='green'
    elif player_choice ==5:
        choice_col='blue'
        
    #print user choice 
    print("user color choice is " + choice_col)
    print("\nNow its computer turn to choose a color.....")


        #computer chooses randomly any number 
        #among 1 ,2 and 3 . Using randint method
        # of random module
    computer_choice = random.randint(1,5)

        #looping until comp_choice value is equal to the choice 
    while computer_choice == player_choice:
        computer_choice = random.randint(1,5)

            #initialize value of compu_choice_col
            #variable corresponding to the computer_choice  value

    if computer_choice ==1:
        computer_choice_col = 'red'
    elif computer_choice ==2:
        computer_choice_col = 'yellow'
    elif computer_choice ==3:
        computer_choice_col='orange'
    elif computer_choice == 4:
        computer_choice_col = 'green'
    elif computer_choice ==5 :
        computer_choice_col = 'blue'
            
    print("Computer color choice is : " + computer_choice_col)


    #condition for winning 
    if(choice_col == computer_choice_col):
        player_score +=1
        print("player_score : "+str(player_score))
        print("computer_score : "+str(computer_score))
    else:
        computer_score +=1
        print("player_score:"+str(player_score))
        print("computer_score: "+str(computer_score))
            
    print("Do you want to play again ? (y/n)")
    answer = input()

    #if user input n or N then condition is True

    if answer == 'n' or answer == 'N':
        break

#after coming out of the while loop
#we print thanks for playing and the overall result of the game.
if computer_score == player_score:
    print("Game is tied")
    print("\n Thanks for playing")
elif computer_score < player_score:
    print("Player is Victorious")
    print("<==User wins ==>")
    print("\n Thanks for playing")
elif computer_score > player_score:
    print("\n<== Computer wins ==>")
    print("\nPlayer is Defeated")
    print("\nThanks for playing")


    
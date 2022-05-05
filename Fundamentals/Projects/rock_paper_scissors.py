import random

def game():
    users_choice = input('Rock, Paper, Scissors...\n')
    opponents_choice = random.choice(['rock','paper','scissors'])
   
    print(f"You picked {users_choice} while your opponent picked {opponents_choice}")
#if it is a tie then run the game again
    if users_choice == opponents_choice:
        print("It's a tie!")
        game()

    #if it is a win then print winning message
    if users_choice == 'rock' and opponents_choice == 'scissors' or users_choice == 'paper' and opponents_choice == 'rock' or users_choice == 'scissors' and opponents_choice == 'paper':
        print("You won the game")
        game()
 #if it is a loss print loss message
    else:
        print('Computer wins! Such rotten luck')
        game()
   
    
    #stop when the player types in stop
    if users_choice == 'stop':
        
        print("Thanks for playing. We hope you had fun")


game()
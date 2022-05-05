import random 

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        #if guess is higher return too high
        if guess > random_number:
            print('Too high. Try again...')
        #if guess is lower return too low 
        elif guess < random_number: 
            print('Too low. Try again...')
        #else return correct
        else:
            print(f'How did you know? You are Correct! The number was {random_number}')




def system_guess(x):
    low = 1
    high = x 
    feedback = ''
    while feedback != 'c':
        if low != high :
            estimation = random.randint(low, high)
        else:
            estimation = low
        feedback = input(f'Is {estimation} too high (H), too low (L) or is it correct (C)?').lower()
        if feedback == 'h':
            high = estimation - 1  
        elif feedback == 'l':
            low = estimation + 1  
    
    print(f'I got it right? Yay. Your number was {estimation}')




system_guess(200)
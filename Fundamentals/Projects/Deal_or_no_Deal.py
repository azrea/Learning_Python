import random
#save the values of prizes in a prize dict 
count = 0
prizes = []
price = [0.01,0.05,0.1,0.5,1,5,10,50,100,250,500,1000,2500,5000,10000,25000,50000,100000,250000,500000,1000000]
choice = 'No deal'
random.shuffle(price)
for i in range(0,len(price)):
    if price[i] > 500:
        new_dict = {'id': i, 'value': price[i], 'color': 'red', 'opened': False}
        prizes.append(new_dict)
    else:
        new_dict = {'id': i, 'value': price[i], 'color': 'blue', 'opened': False}
        prizes.append(new_dict)

#save the ids you want to show the participant in an unopened box list
#unopened_boxes_list = cycle through list and for every dict append the id to the list



#ask user for name 
user_name = input("Enter your name Contestant: \n") 
print(f'Welcome {user_name.capitalize()}')
#ask user to choose between 1 and 21 
user_box = input('Please pick a box from 1 - 20 : \n')
user_box = int(user_box)
#store value as user box
input(f'I hope you are happy with your choice {user_name.capitalize()}, Number {user_box} may not have the money you are looking for and I would hate for you to lose good money on it... \n (Press Enter to continue)')

def show_list():
    unopened_boxes = []
    for x in prizes:
        if x['opened'] == False:
            if x['id'] != user_box:
                unopened_boxes.append(x['id'])
    print(unopened_boxes)
    

show_list()

#reaction function
def reaction(box):
    #print its value with a message matching its color
    print(f"And the value under the box is....\n £{box['value']}")
    if(box['color'] == 'blue'):
        print("Another Blue box off the board. Someone's got good luck.")
    else:
        print('Drat. A Red Box off the board. Not really what you want to see eh?')
    show_list()




#function findthebox 
#take an id 
def locate_box(id):
    #cycle through the list to find the dict with a matching id
    for x in prizes:
        if x['id'] == id:
            if x['opened'] == True or x['id'] == user_box:
                print('Ahh that box has already been opened...awkward')
            else:
                #make it opened : true 
                x['opened'] = True
                specific_box = x
                reaction(specific_box)

#function box picking 
def pick_a_box():
    try: 
        if random.randint(0,len(prizes)) > ((80/100) * len(prizes)):
            #print(random.randint(0,len(prizes)) > ((40/100) * len(prizes)))
            random_value = True
        else:
            random_value = False
        #ask user the number box they want to pick from the unopened id list 
        box_number = int(input('Please pick a box from our list: \n'))
        #once picked give the id to find the box method 
        if(box_number >= 0 or box_number <= 20):
            locate_box(box_number)
        else:
            print('Error...error...Try again ')
        if random_value is True:
            call_banker()
    except ValueError:
        print('That was not a valid number')
    



#callbanker function 
#calculate 75% of the average of the prizes left and offer that

def call_banker():
    sum = calculate_banker_offer()
    print(f'Banker is calling.... \n ...... \n ...... \n Banker offers... \n £{sum}')
    choice = input('Deal...or no Deal: \n').lower()
    if choice == 'deal':
        end_game()
    else:
        game()

def calculate_banker_offer():
    sum = 0 
    for x in prizes:
        if x['opened'] == False:
            sum += x['value']
    sum = sum * 0.75
    sum = int(sum/len(prizes))
    return sum


#congratulation function
#reveal owners box 
#print its value with a message matching its color
def end_game():
    #open all boxes
    for box in prizes:
        if box["opened"] == 'False':
            print(box)
            box['opened'] = 'True'

    print('Congratulations. You finished the game. I hope you are happy with what you got')
    input('Are you ready to see your box... (Press Enter to continue...)')
    print(f'Your box was £{user_box}')

    if choice == 'deal':
        if user_box > calculate_banker_offer():
           print("That was a good choice. The banker will disappounted tonight")
        else:
            print("Better luck next time. The banker won tonight")
    else:
        if user_box > 500:
            print("That's good eh?")
        elif user_box > 10000:
            print("I know you are going home happy tonight. Enjoy your money, buy a boat...Don't buy a boat; They overtax it.")
        elif user_box > 100000:
            print("Arghh, I've been robbed. I'm just joking. Take your money home and welcome to a new tier of wealth.")
        else:
            print("Better luck next time. Should've taken the banker up on his offer")




def check_game():
    #if number of unopened boxes is equal to zero
    count = 0
    for x in prizes:
        if x['opened'] == False:
            count += 1
    if count <= 1:
        return False 
    else:
        return True
   

def game():
    while True:
        pick_a_box()
        print(check_game())
        if check_game() == False:
            break
    end_game()


game()



#if deal change congratulations message 
#have a price section 
#actually end game after end_game() function is called


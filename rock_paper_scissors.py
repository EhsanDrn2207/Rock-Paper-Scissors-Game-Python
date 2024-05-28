import random
with open('result.txt','r') as reader:
    x = reader.read()
    print(x)
    
def intro():
    print("Welcom to our game.")
    print("This is one of the most well known games in the world.")
    print("---Rock, Paper, Scissors---")
    print('-' * 20)

valid_input = ['r', 'p', 's']
dict_selection = {
    'r' : 'Rock',
    'p' : 'Paper',
    's' : 'Scissors'
}

    
def begin_user():
    class InvalidLettersError(Exception):
        pass
    
    while True:
        try:
            user_input = input("Select between Rock, Paper, Scissors:(r/p/s) ")
            print('-' * 20)
            if user_input.isdigit():
                raise ValueError       
            if user_input.lower() not in valid_input:
                raise InvalidLettersError
            user_choice = user_input.lower()
            return user_choice
        
        except InvalidLettersError:
            print("Your input has to one of these itmes(r/p/s), Please try again.")
        except ValueError:
            print("You have not to enter number, Please try again.")

def begin_ai():
    computer_choice = random.choice(valid_input)
    return computer_choice

def process():
    user_score = 0
    ai_score = 0
    
    while user_score != 5 and ai_score != 5:
        
        print(f" user's score: {user_score}\n", f"computer's score: {ai_score}")        
        user_select = begin_user()
        ai_select = begin_ai()
        print(f"Your choice is {dict_selection[user_select]}, Your rival's choice is {dict_selection[ai_select]}.")

        if user_select == ai_select:
            print("Tie")
            print('-' * 20)
             
        elif user_select == 'r' and ai_select == 's':
            print("You gained a score.")
            user_score += 1
            print('-' * 20)

        elif user_select == 's' and ai_select == 'p':
            print("You gained a score.")
            user_score += 1
            print('-' * 20)

        elif user_select == 'p' and ai_select == 'r':
            print("You gained a score.")
            user_score += 1
            print('-' * 20)

        else:
            print("You lost a score.")
            ai_score += 1
            print('-' * 20)
    
    return user_score, ai_score

def winner_and_loser():
    user, ai = process()
    if user == 5:
        print("good job, you won the game!".title())
    else:
        print("sorry, you lost the game.".title())

    def results():
        with open("result.txt", 'a') as writer:
            writer.write(f"*-\nUser's Score:{str(user)}\nComputer's Score:{str(ai)}\n")
            writer.write("-----------------------------------------------\n")
                       
    results()
    
winner_and_loser()
    
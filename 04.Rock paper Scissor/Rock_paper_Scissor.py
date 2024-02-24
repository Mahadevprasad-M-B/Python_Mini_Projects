import random 

def play():
    user = input("What is your choice ?(r) for rock , (p) for paper, (s) for  scissor \n").lower()
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'Its a Tie'

    if is_win(user,computer):
        return 'You won!'
    
    return 'You lost !'

def is_win(user,computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
    or (user == 'p' and computer == 'r'):
         return True
        

print(play())
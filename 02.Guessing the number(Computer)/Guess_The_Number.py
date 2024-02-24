import random

def computerguess(x):
    low = 1
    high = x
    i = 0
    feedback = ''

    while feedback != 'c':
        i = i + 1
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low

        feedback = input(f"Is the guessed number {guess} too high(h), too low(l),correct(c) ").lower()

        if feedback == 'l':
            low = guess + 1 

        elif feedback == 'h':
            high = guess - 1

    print(f"The computer guessed the correct number {guess} in {i} chances")

        

computerguess(20)

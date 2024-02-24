import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    i = 0
    while guess != random_number:
        i += 1
        guess = int(input(f"Enter the random number between 1 and {x}\n"))

        if guess < random_number:
            print("Guessed Number is too low")
        
        elif guess > random_number:
            print("Guessed number is too high")

    
    print(f"Congrats Guessed the currect number {random_number} in {i} chances")


guess(20)
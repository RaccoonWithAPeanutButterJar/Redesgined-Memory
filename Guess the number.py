import random

def guess(x):
    r_num = random.randint(1, x)
    guess = 0
    while guess != r_num: #While u don't guess the number u keep going
        guess = int(input(f"Guess a number between 1 and {x}: "))#Start guessin'
        if guess < r_num:
            print("That's too low....")#Too low of a guess
        elif guess > r_num:
            print("That's too high...")#Too High of a guess
    print(f"Holy moly u did it! U guessed the number {r_num}!")#When u guess correctly then the loop ends and u get this message

def computer_guess(x):#Here the computer tries to guess ur number
    low = 1
    high = x
    feedback = '' #What answer ur gonna give to the computer
    while feedback != 'C':
        if low != high: #If low == high then it breaks :(
            guess = random.randint(low, high)
        else:
            guess = low #It can be either high or low, bcs it's going to be the same number anyways
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)")#Give the PC feedback
        if feedback == 'H':#New parameters
            high = guess - 1
        elif feedback == 'L':#New parameters
            low = guess + 1
    print(f"Damn, the computer guessed the number, it was {guess}!")#The PC did it


computer_guess(100)

#Waleed Iqbal

#import package to use for function
import random


print('---------------------------------')
print('      Guess The Number App       ')
print('---------------------------------')
print()

#Name input

name = input('Player what is your name? ')

# Generate Random Number
randNum = random.randint(0,100)
#setting a number not in range
guess_number = -1


#Define loop to continue unless the number is guessed
while guess_number != randNum:
    # Ask user to guess what the number is
    guess_input = input('Guess a Number between 0 and 100: ')

    # convert input which is a string to an integer so that it cabn be compared to generated random number
    guess_number = int(guess_input)

    if guess_number < randNum:
        print('Sorry {}, your guess of {} was too low.'.format(name, guess_number))
    elif guess_number > randNum:
        print('Sorry {}, your guess of {} was too High.'.format(name, guess_number))
    else:
        print(' GOOD JOB {}, you won! It was {}!'.format(name, guess_number))

print('Done')
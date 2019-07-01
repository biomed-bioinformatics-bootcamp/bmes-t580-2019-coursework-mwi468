
#Waleed Iqbal

#import package to use for function
import random


print('---------------------------------')
print('      Guess That Primer App       ')
print('---------------------------------')
print()

#Name input

name = input('Player what is your name? ')

# Generate Random 5bp primer
goal = random.choice('ACGT')
for i in range(4):
    goal += random.choice('ACGT')
#setting a number not in range
guess = 'NNNNN'


#Define loop to continue unless the primer is guessed
while guess != goal:
    # Ask user to guess what the number is
    guess = input('Guess a 5bp primer: ')
    misses = 0

    for j in range(len(guess)):
        if guess[j] != goal[j]:
            misses += 1

    if misses > 0:
        print('Sorry {} you guessed {} bases wrong'.format(name, misses))
    else:
        print ('GOOD JOB {} You Won!!'.format(name))

print('Done')
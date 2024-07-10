from random import randint

rand_int = randint(1,100)
num_of_guess = 0
subsequent_guess = []
print(rand_int)
while True:
    guess = int(input('Guess a number from 1 to 100: '))

    if guess<1 or guess>100:
        print('Out of Bounds')
        trial = input('Do you want to try again?(y/n): ')
        if trial == 'y':
            continue
        else:
            break
    elif (num_of_guess == 0) and (rand_int != guess):
        if abs(guess-rand_int) < 10:
            print('Warm')
            num_of_guess +=1
            subsequent_guess.append(guess)
            continue
        elif abs(guess-rand_int) > 10:
            print('Cold')
            num_of_guess +=1
            subsequent_guess.append(guess)
            continue
    elif (num_of_guess > 0) and (rand_int != guess):
        if abs(subsequent_guess[num_of_guess-1] - rand_int) > abs(guess - rand_int):
            print('Warmer')
            num_of_guess += 1
            subsequent_guess.append(guess)
            continue
        elif abs(subsequent_guess[num_of_guess-1] - rand_int) < abs(guess - rand_int):
            print('Colder')
            num_of_guess += 1
            subsequent_guess.append(guess)
            continue
    elif rand_int == guess:
        print(f'Congratulations! You have guess the number correctly. It took you {num_of_guess + 1} trial to get it.')
        break



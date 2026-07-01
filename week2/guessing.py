import random as rd

n = rd.randint(1, 10)

incorrect = True
count = 0

while incorrect:
    user_number = int(input('Enter your guess: '))
    count += 1 # count = count + 1

    if user_number == n:
        print('Correct!')
        print(f'Total guesses: {count}')
        incorrect = False
    else:
        print('Incorrect! Try again.')
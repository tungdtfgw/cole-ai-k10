import random as rd

n = rd.randint(1, 100)

incorrect = True
count = 0

while incorrect:
    user_number = int(input('Enter your guess: '))
    count += 1 # count = count + 1

    if user_number == n:
        print('Correct!')
        print(f'Total guesses: {count}')
        incorrect = False
    elif user_number < n:
        print('Incorrect! My number is greater than your guess.')
    else:
        print('Incorrect! My number is less than your guess.')
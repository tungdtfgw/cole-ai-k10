import random as rd

n = int(input('Enter n: '))

incorrect = True
count = 0

lower = 1
upper = 100

while incorrect:
    comp_number = (lower + upper) // 2
    print(f'Computer guess: {comp_number}')
    count += 1

    if comp_number == n:
        print('Correct!')
        print(f'Total guesses: {count}')
        incorrect = False
    elif comp_number < n:
        print('Incorrect! Computer guess is less than user number.')
        lower = comp_number + 1
    else:
        print('Incorrect! Computer guess is greater than user number.')
        upper = comp_number - 1
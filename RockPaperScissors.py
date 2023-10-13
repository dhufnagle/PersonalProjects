import random


win = 0
loss = 0
tie = 0


print('ROCK, PAPER, SCISSORS')
print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')
while True:
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    userChoice = input()

    if userChoice == 'r':
        user = 1
        print('ROCK versus...')
    elif userChoice == 'p':
        user = 2
        print('PAPER versus...')
    elif userChoice == 's':
        user = 3
        print('SCISSORS versus...')
    elif userChoice == 'q':
        exit()
    else:
        print('Please enter a valid input.')
        continue

    optionChoice = [1, 2, 3]
    computer = random.choice(optionChoice)

    if computer == 1:
        print('ROCK')
    elif computer == 2:
        print('PAPER')
    else:
        print('SCISSORS')

    if user == computer:
        print('It is a tie!')
        tie = tie + 1
    elif user == 1 and computer == 2:
        print('You lose!')
        loss = loss + 1
    elif user == 1 and computer == 3:
        print('You win!')
        win = win + 1
    elif user == 2 and computer == 1:
        print('You win!')
        win = win + 1
    elif user == 2 and computer == 3:
        print('You lose!')
        loss = loss + 1
    elif user == 3 and computer == 1:
        print('You lose!')
        loss = loss + 1
    else:
        print('You win!')
        win = win + 1

    print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')

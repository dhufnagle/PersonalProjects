import random, time

win = 0
loss = 0
tie = 0

computerWin = False
userWin = False


def userwin():
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X'



def resetboard(a):
    global board
    a[0] = [1,2,3]
    a[1] = [4,5,6]
    a[2] = [7,8,9]


def resetchoices(b):
    global boardChoices
    b[0:len(boardChoices)] = [1,2,3,4,5,6,7,8,9]


def gameend():
    while True:
        print('Play again? (y/n)')
        gameEndInput = input()
        if gameEndInput == 'y':
            print('\n')
            print('NEW GAME')
        elif gameEndInput == 'n':
            quit()
        else:
            print('Please enter a valid response.')
            continue
        break


print('Tic-Tac-Toe')
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

boardChoices = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in board:
    for j in i:
        print(j, end=" ")
    print()

print('You are X. The computer is O.')

while True:
    print('Enter the number of the spot you would like to play in:')
    userChoice = input()
    try:
        userChoice = int(userChoice)
    except ValueError:
        pass
    if userChoice in boardChoices:
        userChoice = int(userChoice)
        boardChoices.remove(userChoice)
    else:
        print('Please enter a valid response.')
        continue

    if userChoice == 1:
        board[0][0] = 'X'
    elif userChoice == 2:
        board[0][1] = 'X'
    elif userChoice == 3:
        board[0][2] = 'X'
    elif userChoice == 4:
        board[1][0] = 'X'
    elif userChoice == 5:
        board[1][1] = 'X'
    elif userChoice == 6:
        board[1][2] = 'X'
    elif userChoice == 7:
        board[2][0] = 'X'
    elif userChoice == 8:
        board[2][1] = 'X'
    elif userChoice == 9:
        board[2][2] = 'X'

    for i in board:
        for j in i:
            print(j, end=" ")
        print()

    if board[0] == ['X', 'X', 'X']:
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[1] == ['X', 'X', 'X']:
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[2] == ['X', 'X', 'X']:
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        print('Game over. You win!')
        win += 1
        userWin = True
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        print('Game over. You win!')
        win += 1
        userWin = True

    if userWin:
        resetboard(board)
        resetchoices(boardChoices)
        print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')
        gameend()
        userWin = False
        continue

    if not userWin:
        computer = random.choice(boardChoices)
        boardChoices.remove(computer)
        print("Computer's turn:")

        if computer == 1:
            board[0][0] = 'O'
        elif computer == 2:
            board[0][1] = 'O'
        elif computer == 3:
            board[0][2] = 'O'
        elif computer == 4:
            board[1][0] = 'O'
        elif computer == 5:
            board[1][1] = 'O'
        elif computer == 6:
            board[1][2] = 'O'
        elif computer == 7:
            board[2][0] = 'O'
        elif computer == 8:
            board[2][1] = 'O'
        else:
            board[2][2] = 'O'

        time.sleep(1)

        for i in board:
            for j in i:
                print(j, end=" ")
            print()

        if board[0] == ['O', 'O', 'O']:
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[1] == ['O', 'O', 'O']:
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[2] == ['O', 'O', 'O']:
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
            print('Game over. You lose!')
            loss += 1
            computerWin = True
        elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
            print('Game over. You lose!')
            loss += 1
            computerWin = True

    if computerWin:
        resetboard(board)
        resetchoices(boardChoices)
        print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')
        gameend()
        computerWin = False
        continue

    if len(boardChoices) == 0 and not computerWin and not userWin:
        print("Game over. It's a tie!")
        resetboard(board)
        resetchoices(boardChoices)
        tie += 1
        print(win, 'Wins,', loss, 'Losses,', tie, 'Ties')
        gameend()
        computerWin = False
        continue
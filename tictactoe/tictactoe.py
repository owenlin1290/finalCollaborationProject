
# Final Collaborative Project

# Ali Siddiqui



# tictactoe.py




# Requirements:



# Design: (we can only do this part when we are done)




import random


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerName():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    print('ENTER Player 1 name here: ')
    playerName1 = input()
    print()
    print('ENTER Player 2 name here: ')
    playerName2 = input()
    return playerName1, playerName2

def inputPlayerLetter():
    # Lets the player type which letter they want to be.
    # Returns a list with the player's letter as the first item, and the computer's letter as the second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Choose X or O?')
        letter = input().upper()

    # the first element in the tuple is the player1's letter, the second is player2's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst(playerName1, playerName2):
    # Randomly choose the player who goes first.
    if random.randint(0, 1) == 0:
        return playerName1
    else:
        return playerName2


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print()
    print('GAME OVER')
    print('ENTER yes, to restart the game (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def getPlayer1Move(board):
    # Let the player1 type in his move.
    move1 = ' '
    while move1 not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move1)):
        print('' + playerName1 + ', what is your next move? (1-9)')
        move1 = input()
    return int(move1)


def getPlayer2Move(board):
    # Let the player2 type in his move.
    move2 = ' '
    while move2 not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move2)):
        print('' + playerName2 + ', what is your next move? (1-9)')
        move2 = input()
    return int(move2)


def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None



def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10

    playerLetter1, playerLetter2 = inputPlayerLetter()
    playerName1, playerName2 = inputPlayerName()
    turn = whoGoesFirst(playerName1, playerName2 )
    print('' + turn + ' will go first.')


    gameIsPlaying = True

    while gameIsPlaying:
        if turn == playerName1:
            # Player1's turn.
            drawBoard(theBoard)
            move = getPlayer1Move(theBoard)
            makeMove(theBoard, playerLetter1, move)

            if isWinner(theBoard, playerLetter1):
                drawBoard(theBoard)
                print('' + playerName1 + ' has won the game!')
                gameIsPlaying = False
            elif isWinner(theBoard, playerLetter2):
                drawBoard(theBoard)
                print('' + playerName2 + ' has won the game!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = playerName2

        else:
            # Player2's turn.
            drawBoard(theBoard)
            move = getPlayer2Move(theBoard)
            makeMove(theBoard, playerLetter2, move)

            if isWinner(theBoard, playerLetter2):
                drawBoard(theBoard)
                print('' + playerName1 + ' has won!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = playerName1

    if not playAgain():
        break

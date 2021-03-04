# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

import random

magicNumber=10

"""
This function prints out the board that it was passed.
"""
def drawBoard(board):
    print(f"""
 {board[7]} | {board[8]} | {board[9]}
-----------
 {board[4]} | {board[5]} | {board[6]}
-----------
 {board[1]} | {board[2]} | {board[3]}
    """
    )

"""
Lets the player type which letter they want to be.
Returns a list with the player’s letter as the first item, and the computer's letter as the second.
"""
def inputPlayerLetter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = input().upper()

    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

"""
Randomly choose the player who goes first.
"""
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        print(f"The computer will go first.")
        return "computer"
    else:
        print(f"You will go first.")
        return "player"

"""
This function returns True if the player wants to play again, otherwise it returns False.
"""
def playAgain():
    print("Do you want to play again? (Y/N)")
    if input().lower().startswith("y"):
        startGame()


def makeMove(board, letter, move):
    board[move] = letter

"""
Given a board and a player’s letter, this function returns True if that player has won.
We use bo instead of board and le instead of letter so we don’t have to type as much.
"""
def isWinner(bo, le):
    return (
        (bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
        (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
        (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
        (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
        (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
        (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
        (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
        (bo[9] == le and bo[5] == le and bo[1] == le)    # diagonal
    )



"""
Make a duplicate of the board list and return it the duplicate.
"""
def getBoardCopy(board):
    dupeBoard = []

    for i in range(0, len(board)):
        dupeBoard.append(board[i])

    return dupeBoard


"""
Return true if the passed move is free on the passed board.
"""
def isSpaceFree(board, move):
    return board[move] == " "


"""
Let the player type in their move.
"""
def getPlayerMove(board):
    move = None
    while move not in "1 2 3 4 5 6 7 8 9".split()or not isSpaceFree(board, int(move)):
        print("What is your next move? (1-9)")
        move = input()
    return int(move)


"""
Returns a valid move from the passed list on the passed board.
Returns None if there is no valid move.
"""
def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)



"""
Given a board and the computer's letter, 
determine where to move and return that move.
"""
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    """
    Here is our algorithm for our Tic Tac Toe AI:
    First, check if we can win in the next move
    """
    for i in range(1, magicNumber):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    """
    Check if the player could win on their next move, and block them.
    """
    for i in range(1, magicNumber):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    """
    Try to take one of the corners, if they are free.
    """
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, magicNumber):
        if isSpaceFree(board, i):
            return False
    return True

def checkGameOver(theBoard, playerLetter, computerLetter, turn):
    if turn == "player":
        if isWinner(theBoard, playerLetter):
            print("Hooray! You have won the game!")
        if isBoardFull(theBoard):
            print("The game is a tie!")
    else:
        if isWinner(theBoard, computerLetter):
            print("The computer has beaten you! You lose.")
        if isBoardFull(theBoard):
            print("The game is a tie!")

def play(theBoard, playerLetter, computerLetter, turn):
    drawBoard(theBoard)
    if turn == "player":
        # Player’s turn.
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)
        checkGameOver(theBoard, playerLetter, computerLetter, "player")
        play(theBoard, playerLetter, computerLetter, "computer")
    else:
        # Computer’s turn.
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)
        checkGameOver(theBoard, playerLetter, computerLetter, "computer")
        play(theBoard, playerLetter, computerLetter, "player")

def startGame():
    # Reset the board
    theBoard = [" "] * magicNumber
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()

    play(theBoard, playerLetter, computerLetter, turn)


print("Welcome to Tic Tac Toe!")
startGame()
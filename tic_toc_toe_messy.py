# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

import random

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

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

"""
Randomly choose the player who goes first.
"""
def whoGoesFirst():
    if random.randint(0, 1) == 0:
        return "computer"
    else:
        return "player"

"""
This function returns True if the player wants to play again, otherwise it returns False.
"""
def playAgain():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")


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

    for i in range(0, len(board)):  # TODO: Clean this mess!
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
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
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
# TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None:# TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print("Welcome to Tic Tac Toe!")

# TODO: The following mega code block is a huge hairy monster. Break it down
# into smaller methods. Use TODO s and the comment above each section as a guide
# for refactoring.

# Reset the board
theBoard = [" "] * 10  # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
playerLetter, computerLetter = inputPlayerLetter()
turn = whoGoesFirst()
print(f"The {turn} will go first.")
gameIsPlaying = True  # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?)
#       See whether you can get rid of this 'flag' variable. If so, remove it.

while gameIsPlaying:  # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
    #       Use a meaningful name for the function you choose.
    if turn == "player":
        # Player’s turn.
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
        makeMove(theBoard, playerLetter, move)

        if isWinner(theBoard, playerLetter):
            drawBoard(theBoard)
            print("Hooray! You have won the game!")
            gameIsPlaying = False
        if isBoardFull(theBoard):
            drawBoard(theBoard)
            print("The game is a tie!")
            break
        turn = "computer"
    
        

    else:
        # Computer’s turn.
        move = getComputerMove(theBoard, computerLetter)
        makeMove(theBoard, computerLetter, move)

        if isWinner(theBoard, computerLetter):
            drawBoard(theBoard)
            print("The computer has beaten you! You lose.")
            gameIsPlaying = False
        else:  # TODO: is this 'else' necessary?
            if isBoardFull(theBoard):
                drawBoard(theBoard)
                print("The game is a tie!")
                break
            else:  # TODO: Is this 'else' necessary?
                turn = "player"

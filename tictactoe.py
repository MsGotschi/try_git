#global constants
X="X"
O="O"
EMPTY=" "
TIE="tie"
NUMSQRS= 9

def instructions():
    """display the instructions for the game"""
    print('this is how you play... blah blah')

def askYesNo(question):
    """Ask a yes no question"""
    reponse = None
    while response not in ("y","n"):
        reponse = input(question).lower()

    return response

def askNum(question, low, high):
    """ask for a number within a range"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def pieces():
    """Determine if a player or the computer goes first"""
    goFirst = askYesNo('want to go first? y/n')
    if goFirst == 'y':
        print('you go first\n')
        human = X
        computer = 0
    else:
        print('ok, computer goes first')
        human = 0
        computer = X
    return computer, human

def newBoard():
    """create a new game board"""
    board=[]
    for square in range(NUMSQRS):
        board.append(EMPTY)
    return board

def displayBoard(board):
    """display board on screen"""
    print("\n\t",board[0],"|",board[1],"|",board[2])
    print("\t ----------")
    print("\n\t",board[3],"|",board[4],"|",board[5])
    print("\t---------")
    print("\n\t",board[6],"|",board[7],"|",board[8])

def legalMoves(board):
    """create a list of legal moves"""
    moves=[]
    for square in range(NUMSQRS):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """determine a winner"""
    WAYS2WIN = ((0,1,2),(3,4,5,(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for rows in WAYS2WIN:
        if board[row[0]] == board[row[1]]==board[[row2]]!=EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE

    return None
                    

#main program starts here
print('welcome')
instructions()
b=newBoard()
displayBoard(b)


input('\n\npress enter to exit')



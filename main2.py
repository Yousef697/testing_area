from collections import deque
from queue import PriorityQueue

def terminal(board):
    empty = 0
    for i in board:
        for j in i:
            if j == '.':
                empty += 1
    if empty == 0:
        return True
    
    for i in board:
        if i[0] == i[1] and i[1] == i[2] and i[0] != '.':
            return True
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '.':
            return True
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '.':
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '.':
        return True
    return False
def utility(board):
    for i in board:
        if i[0] == i[1] and i[1] == i[2] and i[0] != '.':
            return 1 if i[0] == 'X' else -1
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != '.':
            return 1 if board[0][i] == 'X' else -1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '.':
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '.':
        return 1 if board[0][2] == 'X' else -1
    return 0
def actions(board, player):
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                new_board = [list(board[i]) for i in range(3)]
                new_board[i][j] = player
                action.append(new_board)
    return action
def minimax(board, player):
    if terminal(board):
        return utility(board)
    
    act = actions(board, player)
    ans = -100 if player == 'X' else 100

    for b in act:
        cand = minimax(b, 'O' if player == 'X' else 'X')
        if player == 'X':
            ans = max(ans, cand)
        else:
            ans = min(ans, cand)
    return ans
def tic_tac_toe(board):
    x, o, empty = 0, 0, 0

    for i in board:
        for j in i:
            if j == 'X':
                x += 1
            elif j == 'O':
                o += 1
            else:
                empty += 1

    if x < o or x > o + 1:
        return False
    
    if (x == o):
        return minimax(board, 'X')
    return minimax(board, 'O')

n = 3
grid = [list(input().strip()) for _ in range(n)]
for i in grid:
    print(i)
print(tic_tac_toe(grid))

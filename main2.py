from collections import deque
from queue import PriorityQueue
    
def bfs(g):
    n, m = len(g), len(g[0])
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'A':
                start_x, start_y = i, j
            if g[i][j] == 'B':
                end_x, end_y = i, j

    visited = [[False] * m for i in range(n)]
    parent = [[(-1, -1) for j in range(m)] for i in range(n)]

    def valid(x, y):
        return 0 <= x and x < n and 0 <= y and y < m and g[x][y] != '#' and not visited[x][y]
    
    q = deque()
    q.append((start_x, start_y))

    while len(q) != 0:
        cur_x, cur_y = q.popleft()

        if cur_x == end_x and cur_y == end_y:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cur_x + dx, cur_y + dy
            if valid(nx, ny):
                visited[nx][ny] = True
                parent[nx][ny] = (cur_x, cur_y)
                q.append((nx, ny))

    if not visited[end_x][end_y]:
        return [(-1, -1)]
    
    path = [(end_x, end_y)]
    while (start_x, start_y) != (end_x, end_y):
        px, py = parent[end_x][end_y]
        path.append((px, py))
        end_x, end_y = px, py
    return path[::-1]
def dfs(g):
    n, m = len(g), len(g[0])
    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'A':
                start_x, start_y = i, j
            if g[i][j] == 'B':
                end_x, end_y = i, j

    visited = [[False] * m for i in range(n)]
    parent = [[(-1, -1) for j in range(m)] for i in range(n)]

    def valid(x, y):
        return 0 <= x and x < n and 0 <= y and y < m and g[x][y] != '#' and not visited[x][y]
    
    q = deque()
    q.append((start_x, start_y))

    while len(q) != 0:
        cur_x, cur_y = q.pop()

        if cur_x == end_x and cur_y == end_y:
            break

        for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            nx, ny = cur_x + dx, cur_y + dy
            if valid(nx, ny):
                visited[nx][ny] = True
                parent[nx][ny] = (cur_x, cur_y)
                q.append((nx, ny))

    if not visited[end_x][end_y]:
        return [(-1, -1)]
    
    path = [(end_x, end_y)]
    while (start_x, start_y) != (end_x, end_y):
        px, py = parent[end_x][end_y]
        path.append((px, py))
        end_x, end_y = px, py
    return path[::-1]
def a_star(g):
    n, m = len(g), len(g[0])

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    for i in range(n):
        for j in range(m):
            if g[i][j] == 'A':
                start_x, start_y = i, j
            if g[i][j] == 'B':
                end_x, end_y = i, j

    def valid(x, y):
        return 0 <= x and x < n and 0 <= y and y < m and g[x][y] != '#' and not visited[x][y]
    
    def h(x, y):
        return abs(x - end_x) + abs(y - end_y)
    def k(cells):
        return cells + 1
    
    pq = PriorityQueue()
    visited = [[False] * m for i in range(n)]
    parent = [[(-1, -1) for j in range(m)] for i in range(n)]
    pq.put((0, 0, start_x, start_y, start_x, start_y))

    while not pq.empty():
        cost, cells, cur_x, cur_y, parent_x, parent_y = pq.get()

        if visited[cur_x][cur_y]:
            continue

        # print(cur_x, cur_y)
        visited[cur_x][cur_y] = True
        parent[cur_x][cur_y] = (parent_x, parent_y)
        if cur_x == end_x and cur_y == end_y:
            break

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cur_x + dx, cur_y + dy
            if valid(nx, ny):
                pq.put((h(nx, ny) + k(cells), k(cells), nx, ny, cur_x, cur_y))

    if not visited[end_x][end_y]:
        return [(-1, -1)]
    
    path = [(end_x, end_y)]
    while (start_x, start_y) != (end_x, end_y):
        px, py = parent[end_x][end_y]
        path.append((px, py))
        end_x, end_y = px, py
    return path[::-1]
# n, m = map(int, input().split())
# grid = [[] for i in range(n)]
# for i in range(n):
#     grid[i] = input()
# print(len(a_star(grid)))
# print(a_star(grid))

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
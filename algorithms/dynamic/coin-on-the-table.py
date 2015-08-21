MAX_INT = 2**64

def find_goal(board):
    for i,row in enumerate(board):
        for j,col in enumerate(board[i]):
            if col == '*':
                return i,j
    return -1,-1

def min_operations(board, K):
    min_ops = list(list(list(0 for i in range(K+1)) for j in range(len(board[0]))) for i in range(len(board)))

    for k in range(K+1):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if k == 0:
                    min_ops[i][j][k] = 0 if i == 0 and j == 0 else MAX_INT
                else:
                    p = min_ops[i][j][k-1]
                    u = min_ops[i-1][j][k-1] + (0 if board[i-1][j] == 'D' else 1) if i > 0 else MAX_INT
                    d = min_ops[i+1][j][k-1] + (0 if board[i+1][j] == 'U' else 1) if i < len(board)-1 else MAX_INT
                    l = min_ops[i][j-1][k-1] + (0 if board[i][j-1] == 'R' else 1) if j > 0 else MAX_INT
                    r = min_ops[i][j+1][k-1] + (0 if board[i][j+1] == 'L' else 1) if j < len(board[0])-1 else MAX_INT
                    min_ops[i][j][k] = min(p,u,d,l,r)
    i,j = find_goal(board)
    ops = min_ops[i][j][K]
    return ops if ops < MAX_INT else -1

n,m,k = list(map(int, input().split()))
board = list()
for i in range(n):
    board.append(input().strip())
print(min_operations(board, k))

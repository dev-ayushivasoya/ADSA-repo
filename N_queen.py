def N_Queen(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if N_Queen(board, row, col, n):
            board[row] = col

            if solve(board, row + 1, n):
                return True

            board[row] = -1

    return False


n = int(input("Enter number of queens: "))
board = [-1] * n

if solve(board, 0, n):
    print("Solution:")
    for i in range(n):
        for j in range(n):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print("-", end=" ")
        print()
else:
    print("No solution exists")

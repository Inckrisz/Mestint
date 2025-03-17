def print_solution(board):
    """Kiírja a megoldást egy N×N-es mátrixban"""
    for row in board:
        print(" ".join(str(cell) for cell in row))
    print("\n")


def is_safe(board, row, col, n):
    """Ellenőrzi, hogy a királynő elhelyezhető-e a (row, col) pozícióban"""
    
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, n):
    """Rekurzív függvény, amely próbálja elhelyezni a királynőket a mátrixban"""
    if row == n:
        print_solution(board)  
        return True

    for col in range(n):
        if is_safe(board, row, col, n):  
            board[row][col] = 1  


            solve_n_queens(board, row + 1, n)


            board[row][col] = 0  


def n_queens(n):
    """Fő függvény, amely inicializálja a mátrixot és elindítja a keresést"""
    board = [[0] * n for _ in range(n)]  
    solve_n_queens(board, 0, n)  

n_queens(4)

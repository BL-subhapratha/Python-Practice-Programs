def print_matrix(matrix):
    for i in range(3):
        for j in range(3):
            print(f"{matrix[i][j]} |", end=" ")
        print()

matrix = [["","",""],["","",""],["","",""]]
row = int(input("Enter row: "))
col = int(input("Enter column: "))

matrix[row][col] = 'X'
print_matrix(matrix)
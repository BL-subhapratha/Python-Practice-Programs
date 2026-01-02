m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

matrix = []
for i in range(m):
    rows = []
    for j in range(n):
        element = int(input(f"Enter the element for row {i+1} and column {j+1}: "))
        rows.append(element)
    matrix.append(rows)
print("The elements in the array are: ")
for i in matrix:
    print(i)

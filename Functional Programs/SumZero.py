n = int(input("Enter the size of the list:"))
arr = []
for i in range(n):
    element = int(input(f"Enter the element for {i+1}:"))
    arr.append(element)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i] + arr[j] + arr[k] == 0:
                print(f"({arr[i]} + {arr[j]} + {arr[k]})")
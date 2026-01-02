n = int(input("Enter a number: "))
if n >= 0 and n < 31:
    for i in range(1, n):
        print(2**i)
else:
    print("Invalid number!")
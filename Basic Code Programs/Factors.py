n = int(input("Enter a number: "))

i = 1
while i*i <= n:
    if n % i == 0:
        print(i)
    i = i+1
year = int(input("Enter a year: "))
n = year
count = 0
while(n > 0):
    n = n//10
    count += 1
if count == 4:
    if year % 4 == 0 or year % 400 == 0:
        print("Leap Year!")
    else:
        print("Not a Leap Year!")
else:
    print("Invalid Year!")
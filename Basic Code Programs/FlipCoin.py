import random
head = 0
tail = 0
n = int(input("Enter number of times to flip coin: "))
for i in range(n):
    flip = random.random()
    if flip < 0.5:
        tail = tail + 1
    else:
        head = head + 1
print("Percentage of head:", head/n*100)
print("Percentage of tail:",tail/n*100)
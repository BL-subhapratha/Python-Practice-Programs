import random

coupons = []
count = 0

num = int(input("Enter the number of distinct coupons needed: "))

while(len(coupons) < num):
    rand_num = random.randint(1,100)
    if rand_num not in coupons:
        coupons.append(rand_num)
    count += 1

print(coupons)
print(f"Total number of times random number was generates is {count}")

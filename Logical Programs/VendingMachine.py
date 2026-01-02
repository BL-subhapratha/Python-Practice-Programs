import math

worth = float(input("Enter the worth of the product purchased (Rs): "))
amount = float(input("Enter the amount inserted (Rs): "))

# Convert to paise
worth_paise = int(round(worth * 100))
amount_paise = int(round(amount * 100))

balance = amount_paise - worth_paise

if balance < 0:
    print("Insufficient amount inserted.")
else:
    print("Balance amount to be returned:", balance, "paise")

    coins = [100, 50, 25, 10, 5, 1]  # in paise

    for coin in coins:
        count = balance // coin
        if count > 0:
            print(f"{count} coin(s) of {coin} paise")
            balance = balance % coin
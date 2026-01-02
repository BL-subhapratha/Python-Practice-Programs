import random

stake = int(input("Enter the stake: "))
goal = int(input("Enter the goal: "))
num = int(input("Enter the number of times: "))

win = 0
lose = 0

for i in range(num):
    game =  random.random()
    print(f"{(i+1)} - {game} - Stake value is {stake}")
    if game <= 0.5:
        lose += 1
        stake -=1
        if stake < 0: 
            print("You lose!") 
            break
    else:
        win +=1
        stake +=1
        if stake == goal: 
            print("You win!")
            break
print(f"Total win percentage is {(win/num)*100} and total lose percentage is {(lose/num)*100}")
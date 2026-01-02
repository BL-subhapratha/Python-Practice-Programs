import time

print("Press the ENTER key to start the timer...")
input()

start = time.time()

print("Press the ENTER key to stop the timer...")
input()

stop = time.time()

print("The elapsed time is ", stop-start)
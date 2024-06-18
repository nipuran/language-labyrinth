import datetime
import time
import os

def clear_screen():
    # Clear the console in a cross-platform way
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix-based systems

set_time = 120  # seconds

now = datetime.datetime.now()
timer = now + datetime.timedelta(seconds=set_time)

print("Timer set for:", timer.time())

while True:
    time_left = timer - datetime.datetime.now()
    seconds_left = time_left.total_seconds()

    if seconds_left <= 0:
        print("Time is up")
        break

    print(f"Time left: {int(seconds_left)} seconds", end='\r', flush=True)
    time.sleep(1)
    clear_screen()



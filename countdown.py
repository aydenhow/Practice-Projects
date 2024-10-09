# countdown.py #
# Countdown timer program prompts for countdown time and counts per second until end.

from time import sleep

# seconds countdown #
#start_time = input("Countdown from (MM:SS): ")
#start_time = start_time.split(":")
#seconds = int(start_time[0])
#seconds += 60*int(start_time[0]) - 1
#while seconds != 0:
#    print(seconds)
#    seconds -= 1
#    sleep(1)
#if seconds == 0:
#    print("Time is up!")

start_time = input("Countdown from (MM:SS): ")
current_time = start_time.split(":")
minutes = int(current_time[0])
seconds = int(current_time[1])
while seconds >= 60:
    minutes += 1
    seconds -= 60
while minutes != 0 or seconds != 0:
    if 0 < minutes < 10 <= seconds:
        print(f"{minutes}:{seconds}")
    elif 0 < seconds < 10:
        print(f"{minutes}:0{seconds}")
    elif 0 < seconds < 10:
        print(f"{minutes}:0{seconds}")
    elif seconds == 0:
        print(f"{minutes}:00")
    else:
        print(f"{minutes}:{seconds}")
    if seconds != 0:
        seconds -= 1
    else:
        minutes -= 1
        seconds += 59
    sleep(1)
print("0:00")
print("Time is up!")

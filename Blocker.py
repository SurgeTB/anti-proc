import psutil
import time

number_machine_broke = 1

while number_machine_broke != 0:
    finish1 = input("Enter time to run for (e.g. 1s, 5m, 1h): ")
    if finish1[-1:] == "s":
        finish_final = int(finish1[:-1])
        number_machine_broke = 0
    elif finish1[-1:] == "m":
        finish_final = int(finish1[:-1]) * 60
        number_machine_broke = 0
    elif finish1[-1:] == "h":
        finish_final = int(finish1[:-1]) * 3600
        number_machine_broke = 0
    elif finish1[-1:] == "d":
        finish_final = int(finish1[:-1]) * 86400
        number_machine_broke = 0

print("\nRunning for", str(finish_final), "seconds...\n")

block = ["discord", "toribash", "epic", "blizzard", "steam", "overwatch", "league", "lol", "battle"] #add things to block here....

start = time.time()

elapsed = 0

while elapsed < finish_final:
    time.sleep(2)
    for p in psutil.process_iter():
        for check in block:
            if check in (p.name()).lower():
                print(time.strftime("%H:%M"), "- Closed", p.name())
                try:
                    p.kill()
                except:
                    print(time.strftime("%H:%M"), "- Failed to close", p.name())
                break

    elapsed = time.time() - start

print("\nFinished!")


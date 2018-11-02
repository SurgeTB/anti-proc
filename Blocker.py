import psutil
import time
import sys, subprocess
from plyer import notification

block = ["toribash", "discord", "steam", "battle", "overwatch", "blizzard", "borderlands", "watch"] # add things to block here....

last_not = 0

while 1:
    for p in psutil.process_iter():
        time.sleep(0.01) # leave a timer so it's not too system intensive
        if p.name().lower()[:-4] in block: # should the process be blocked?
            try:
                if time.time() - last_not > 3 or last_not == 0: # make sure we're not sending notifications too quickly, to avoid spam
                    notification.notify(title=(p.name()[:-4]+ " closed "), message=str(time.strftime("%H:%M")+" - Closed "+ p.name()), app_name="Python Blocker")
                    # send a desktop notification when something gets closed
                last_not = time.time() # make a note of when the last notification was sent
                p.kill() # close the process
                print(time.strftime("%H:%M"), "- Closed", p.name()) # successfully closed
            except:
                print(time.strftime("%H:%M"), "- Failed to close", p.name()) # error
                
            
            



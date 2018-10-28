import psutil
import time
import sys, subprocess

subprocess.call([sys.executable, "-m", "pip", "install", "plyer"])

from plyer import notification

block = ["toribash", "discord", "steam", "battle", "overwatch", "blizzard", "borderlands", "watch"] #add things to block here....
last_not = 0

while 1:
    for p in psutil.process_iter():
        time.sleep(0.01)
        if p.name().lower()[:-4] in block:
            try:

                if time.time() - last_not > 3 or last_not == 0:
                    notification.notify(title=(p.name()[:-4]+ " closed "), message=str(time.strftime("%H:%M")+" - Closed "+ p.name()), app_name="Python Blocker")
                    
                last_not = time.time()
                p.kill()
                print(time.strftime("%H:%M"), "- Closed", p.name())
            except:
                print(time.strftime("%H:%M"), "- Failed to close", p.name())
                
            
            



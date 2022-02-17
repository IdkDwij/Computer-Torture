from threading import Thread
import os
something = 0

def sdfghjk():
    print("Running " ,something, "Threads")
    while True:
        os.system("ping -t localhost")


while True:
    something += 1
    thread = Thread(target=sdfghjk)
    thread.start()


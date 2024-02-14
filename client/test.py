from client import Client
import time
from threading import Thread

c1 = Client("Yonela")
c2 = Client("Fannie")

def update_messages():
    msgs = []
    run = True
    while run:
        time.sleep(0.5)
        new_messages = c1.get_messages()
        msgs.extend(new_messages)
        for msg in new_messages:
            print(msg)
            if msg == "{quit}":
                run = False
                break

Thread(target=update_messages).start()

c1.send_message("boizens")
time.sleep(5)
c2.send_message("What's up")
time.sleep(5)

c1.send_message("nothing much, how about you?")
time.sleep(5)
c2.send_message("Boring boizens! Code?</>:)")

time.sleep(5)

c1.send_message("Nothing much :(!, Any new projects ?")
time.sleep(5)
c2.send_message("No boizens!!")

time.sleep(7)

c1.disconnect()
time.sleep(7)
c2.disconnect()
from pypresence import Presence
import time
import random

client_id = '64567352374564'  # Fake Client ID, place your own.
RPC = Presence(client_id)  # Initialize the client class
RPC.connect() # Start the handshake loop

while True:  # The presence will stay on as long as the program is running
    with open("bible.txt", "r") as f:
        for line in f.readlines():
            verse = line
            RPC.update(details="Verse" + str(random.randint(0,1600)) + ":", state=verse)
            print(verse)
            time.sleep(15) # Can only update rich presence every 15 seconds
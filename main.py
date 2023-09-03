from instagrapi import Client;
from time import sleep;
import datetime;
import os;

ACCOUNT_USERNAME = os.environ['ACCOUNT_USERNAME']
ACCOUNT_PASSWORD = os.environ['ACCOUNT_PASSWORD']

cl = Client();
cl.login(username=ACCOUNT_USERNAME, password=ACCOUNT_PASSWORD);

print(cl.sessionid);

previous_min = 0;

def updateNote(currentTime: str):
    cl.create_note(currentTime);


while True:
    now = datetime.datetime.now();
    currentTime = now.strftime("%I:%M %p");
    current_minutes = now.strftime("%M")
    current_seconds = now.strftime("%S");

    if (current_minutes == previous_min):
        remaining_seconds = 60 - int(current_seconds);
        print("Sleeping for " + str(remaining_seconds) + " seconds");
        sleep(remaining_seconds);
        continue;
    else:
        previous_min = current_minutes;
        print("A minute has passed. " + str(current_minutes))
        updateNote(currentTime);
        
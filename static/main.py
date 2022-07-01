
from plyer import notification
import time

if __name__ == "__main__":
    while True:
        notification.notify(title = "Drink water " , message = "drink water its another 15 minutes" , timeout = 5 )
        time.sleep(900)

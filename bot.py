from datetime import datetime
import webbrowser
from pynput.mouse import Button, Controller
import time

mouse = Controller()


monday = [
    ("16:22:00", "https://www.google.com"),
    ("16:42:00", "https://www.google.com"),
    ("17:50:00", "https://www.google.com"),
]

tuesday = [
    ("15:40:00", "https://www.google.com"),
    ("15:42:00", "https://www.google.com"),
    ("16:50:00", "https://www.google.com"),
]


wednesday = [
    ("15:40:00", "https://www.google.com"),
    ("15:42:00", "https://www.google.com"),
    ("16:50:00", "https://www.google.com"),
]


thursday = [
    ("15:40:00", "https://www.google.com"),
    ("15:42:00", "https://www.google.com"),
    ("16:50:00", "https://www.google.com"),
]

friday = [
    ("15:40:00", "https://www.google.com"),
    ("15:42:00", "https://www.google.com"),
    ("16:50:00", "https://www.google.com"),
]


schedule = [
    monday,
    tuesday,
    wednesday,
    thursday,
    friday,
    "saturday",
    "sunday"
]


def joinClass(link):
    webbrowser.open(link)

    # Set pointer position
    time.sleep(5)
    mouse.position = (1418, 693)
    mouse.click(Button.left, 1)


x = 0

while x < 2:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    weekday = datetime.today().weekday()

    print(current_time)

    routine = schedule[weekday]

    #print("Timings : ")
    for y in routine:
        # print(y[0])

        if(y[0] == current_time):
            joinClass(y[1])

    time.sleep(1)

import time
from pynput import mouse
import keyboard

# Define the coordinates to click
x = 476
y = 624

print("Press s to start...")
while not keyboard.is_pressed('s'):
    pass

while True:
    # Click at the coordinates 8 times
    for i in range(9):
        mouse.Controller().position = (x, y)
        mouse.Controller().click(mouse.Button.left)
        time.sleep(0.5)

    # Wait for 5 minutes
    print("Waiting for cooldowns")
    time.sleep(300)
    print("Cooldowns done")

    # Check if the `q` key has been pressed
    if keyboard.is_pressed('q'):
        break

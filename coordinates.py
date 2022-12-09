from pynput import mouse
from PIL import ImageGrab
from time import sleep
def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"Pixel coordinates: ({x}, {y})")
        sleep(0.5)
        # Get the color value of the screen at the coordinates (x, y)
        im = ImageGrab.grab()
        color = im.getpixel((x, y))
        print(f"Color value: {color}")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
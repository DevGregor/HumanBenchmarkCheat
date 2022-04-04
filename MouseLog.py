from pynput.mouse import *

def on_move(x, y):
    print(x, y)
    
def on_click(x, y, button, pressed):
    print(x, y, button, pressed)
    
def on_scroll(x, y, dx, dy):
    print(x, y, dx, dy)

with Listener(on_click=on_click) as listener:
    listener.join()
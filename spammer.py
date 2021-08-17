from pynput.keyboard import Key, Controller
import time
Keyboard = Controller()
time.sleep(5)
while True:
    for letter in "im playin wit u cuh":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)

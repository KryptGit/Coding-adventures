import pynput
import time
import keyboard
x =  int(input("how many cycles"))
time.sleep(10)
while x < 0:
    keyboard.write("pls fish")
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.write("pls sell fish max")
    keyboard.press_and_release('enter')
    keyboard.write("pls beg")
    keyboard.press_and_release('enter')
    keyboard.write("pls pm")
    keyboard.press_and_release('enter')
    time.sleep(3)
    keyboard.write("i")
    keyboard.press_and_release('enter')
    keyboard.write("pls hunt")
    keyboard.press_and_release('enter')
    time.sleep(45)
    x-1

import tkinter as tk

running = False
hours, minutes, seconds, milliseconds = 0, 0, 0, 0
laps = 0
def update():
    global hours, minutes, seconds, milliseconds
    milliseconds += 1
    if milliseconds == 66:
        seconds += 1
        milliseconds = 0
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0

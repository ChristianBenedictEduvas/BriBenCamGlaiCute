# varibales are milliseconds, seconds, minutes, and hours
# needs start, stop, split, and reset
# can add other features 
# we'll utilize Tkinter for import to run GUI

import tkinter as tk
import time 

running = False
hours, minutes, seconds, milliseconds = 0, 0, 0, 0

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

    global hours, minutes, seconds, milliseconds
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    stopwatch_label.configure(text='00:00:00:00')

def update():
    global hours, minutes, seconds, milliseconds
    time.sleep(0.0075)
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
    
    
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string =f'{seconds}' if seconds > 9 else f'0{seconds}'
    milliseconds_string =f'{milliseconds}' if milliseconds > 9 else f'0{milliseconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string + '.' + milliseconds_string)
    global update_time
    update_time = stopwatch_label.after(1, update)


root = tk.Tk()
root.geometry('630x800')
root.title('Stopwatch')
root.configure(bg="white")

stopwatch_label = tk.Label(text='00:00:00:00', font=('Arial', 80, 'bold'))
stopwatch_label.pack()


start_button = tk.Button(text='Start', height=5, width=7, font=('Arial', 20, 'bold',), borderwidth='5', command=Start)
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='Pause', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=Pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='Reset', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=Reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='Quit', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=Quit)
quit_button.pack(side=tk.LEFT)


root.mainloop()
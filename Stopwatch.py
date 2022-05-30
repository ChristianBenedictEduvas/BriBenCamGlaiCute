import tkinter as tk

running = False
hours, minutes, seconds, milliseconds = 0, 0, 0, 0
laps = 0
#put code for start
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
        
        

    global hours, minutes, seconds, milliseconds
    global laps
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    laps = 0
    stopwatch_label.config(text='00:00:00.00')
    split1.configure(text='00:00:00.00')
    split2.configure(text='00:00:00.00')
    split3.configure(text='00:00:00.00')
    split4.configure(text='00:00:00.00')
    split5.configure(text='00:00:00.00')
    split6.configure(text='00:00:00.00')
    split7.configure(text='00:00:00.00')
    split8.configure(text='00:00:00.00')
    split9.configure(text='00:00:00.00')
    split10.configure(text='00:00:00.00') 
    stopwatch_label.configure(text='00:00:00.00')

def split():

    global running

    if running:

        global laps

        laps += 1

        if laps == 1:

            split1.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 2:

            split2.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 3:

            split3.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 4:

            split4.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 5:

            split5.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 6:

            split6.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 7:

            split7.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 8:

            split8.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 9:

            split9.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

        elif laps == 10:

            split10.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)


def split():
    global running
    if running:
        global laps
        laps += 1
        if laps == 1:
            split1.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 2:
            split2.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 3:
            split3.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 4:
            split4.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 5:
            split5.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 6:
            split6.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 7:
            split7.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 8:
            split8.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 9:
            split9.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)
        elif laps == 10:
            split10.configure(text = hours_split + ':' + minutes_split + ':' + seconds_split + "." + milliseconds_split)

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
    
    global hours_split, minutes_split, seconds_split, milliseconds_split
    hours_split = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_split = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_split =f'{seconds}' if seconds > 9 else f'0{seconds}'
    milliseconds_split =f'{milliseconds}' if milliseconds > 9 else f'0{milliseconds}'
    stopwatch_label.config(text=hours_split + ':' + minutes_split + ':' + seconds_split + '.' + milliseconds_split)
    global update_time
    update_time = stopwatch_label.after(10, update)


root = tk.Tk()
root.geometry('630x800')
root.title('Stopwatch')
root.configure(bg='black')

stopwatch_label = tk.Label(text='00:00:00.00', font=('Arial', 86, 'bold'))
stopwatch_label.pack()

# label to display time

# Laps
split1 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split1.pack()
split2 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split2.pack()
split3 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split3.pack()
split4 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split4.pack()
split5 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split5.pack()
split6 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split6.pack()
split7 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split7.pack()
split8 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split8.pack()
split9 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split9.pack()
split10 = tk.Label(text="00:00:00.00", font=("Arial", 25, 'bold'), height="1")
split10.pack()

start_button = tk.Button(text='Start', height=5, width=7, font=('Arial', 20, 'bold',), borderwidth='5', command=start)
start_button.pack(side=tk.LEFT)
split_button = tk.Button(text='Split', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=split)
split_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='Stop', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=pause)
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='Reset', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=reset)
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='Exit', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=quit)
quit_button.pack(side=tk.LEFT)


root.mainloop()

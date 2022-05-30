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
root.mainloop()

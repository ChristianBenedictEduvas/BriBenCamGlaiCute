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

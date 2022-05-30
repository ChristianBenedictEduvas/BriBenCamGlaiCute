def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
pause_button = tk.Button(text='Stop', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=pause)
pause_button.pack(side=tk.LEFT)

def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

reset_button = tk.Button(text='Reset', height=5, width=7, font=('Arial', 20, 'bold'), borderwidth='5', command=reset)
reset_button.pack(side=tk.LEFT)

def start():
    global running
    if not running:
        update()
        running = True

start_button = tk.Button(text='Start', height=5, width=7, font=('Arial', 20, 'bold',), borderwidth='5', command=start)
start_button.pack(side=tk.LEFT)

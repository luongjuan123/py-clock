import tkinter as tk
import time
import math
from datetime import datetime
import winsound

def update_clock():
    now = datetime.now()
    hours, minutes, seconds = now.hour, now.minute, now.second
    draw_clock_face()
    draw_hand((hours % 12) * 30 + minutes * 0.5, 50, "black")  # Kim giờ
    draw_hand(minutes * 6, 70, "blue")  # Kim phút
    draw_hand(seconds * 6, 80, "red")  # Kim giây
    root.after(1000, update_clock)

def draw_clock_face():
    canvas.delete("hands")
    canvas.create_oval(50, 50, 250, 250, outline="black", width=3)
    for i in range(12):
        angle = math.radians(i * 30)
        x1, y1 = 150 + math.cos(angle) * 90, 150 - math.sin(angle) * 90
        x2, y2 = 150 + math.cos(angle) * 100, 150 - math.sin(angle) * 100
        canvas.create_line(x1, y1, x2, y2, width=2)
        x_text, y_text = 150 + math.cos(angle) * 75, 150 - math.sin(angle) * 75
        canvas.create_text(x_text, y_text, text=str(i if i else 12), font=("Arial", 12, "bold"))

def draw_hand(angle, length, color):
    angle = math.radians(angle - 90)
    x, y = 150 + math.cos(angle) * length, 150 + math.sin(angle) * length
    canvas.create_line(150, 150, x, y, width=4, fill=color, tags="hands")

def start_stopwatch():
    global stopwatch_running
    if not stopwatch_running:
        stopwatch_running = True
        run_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_time
    stopwatch_running = False
    stopwatch_time = 0
    stopwatch_label.config(text="00:00:00")

def run_stopwatch():
    global stopwatch_time
    if stopwatch_running:
        stopwatch_time += 1
        minutes, seconds = divmod(stopwatch_time, 60)
        hours, minutes = divmod(minutes, 60)
        stopwatch_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        #winsound.Beep(1000, 200)  
        root.after(1000, run_stopwatch)

# GUI
root = tk.Tk()
root.title("Clock & Stopwatch")
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()
stopwatch_label = tk.Label(root, text="00:00:00", font=("Arial", 20))
stopwatch_label.pack()
btn_frame = tk.Frame(root)
btn_frame.pack()
stopwatch_time = 0
stopwatch_running = False

start_btn = tk.Button(btn_frame, text="Start", command=start_stopwatch)
stop_btn = tk.Button(btn_frame, text="Stop", command=stop_stopwatch)
reset_btn = tk.Button(btn_frame, text="Reset", command=reset_stopwatch)
start_btn.pack(side="left")
stop_btn.pack(side="left")
reset_btn.pack(side="left")

update_clock()
root.mainloop()
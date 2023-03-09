import RPi.GPIO as GPIO
import tkinter as tk
import threading
import time
import pyaudio
import wave
import os
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import queue

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
sound = 23
sound2 = 24
GPIO.setup(sound, GPIO.IN)
GPIO.setup(sound2, GPIO.IN)
n = 0
class VoiceRecorder(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("SnoringRecorder")
        self.master.geometry("500x200")
        self.hours = tk.StringVar()
        self.minutes = tk.StringVar()
        self.seconds = tk.StringVar()
        self.hours.set("00")
        self.minutes.set("00")
        self.seconds.set("00")
        self.timer_running = False
        self.count = 0  # Initialize the counter to zero

        # Create the widgets
        
        trackframe = tk.LabelFrame(self.master,text="RECORD",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=tk.GROOVE)
        trackframe.place(x=0,y=0,width=500,height=200)

        self.label_hours = tk.Label(trackframe,textvariable=self.hours, font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_hours.grid(row=0, column=0)
        self.label_colon1 = tk.Label(trackframe,text=":", font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_colon1.grid(row=0, column=1)
        self.label_minutes = tk.Label(trackframe,textvariable=self.minutes, font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_minutes.grid(row=0, column=2)
        self.label_colon2 = tk.Label(trackframe,text=":", font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_colon2.grid(row=0, column=3)
        self.label_seconds = tk.Label(trackframe,textvariable=self.seconds, font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_seconds.grid(row=0, column=4)
        
        # Add a label to display the count
        self.label_count = tk.Label(trackframe,text="Number of times snoring: {}".format(self.count), font=("times new roman",20,"bold"),bg="grey",fg="white",bd=5)
        self.label_count.grid(row=1, columnspan=5)

        # Start the timer automatically
        self.start_timer()

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.remaining_time = 0
            self.update_time()

    def update_time(self):
        hours = self.remaining_time // 3600
        minutes = (self.remaining_time % 3600) // 60
        seconds = self.remaining_time % 60
        self.hours.set("{:02d}".format(hours))
        self.minutes.set("{:02d}".format(minutes))
        self.seconds.set("{:02d}".format(seconds))
        self.remaining_time += 1
        self.master.after(1000, self.update_time)

    def callback(self, sound):
        if GPIO.input(sound) == 0:
            print(GPIO.input(sound))
            threading.Thread(target=self.record).start()
            time.sleep(35)
        else:
            print(GPIO.input(sound))
            
    def callback2(self, sound2):
        global n
        if GPIO.input(sound2) == 0:
            global n
            if (n == 0):
                n += 1    
            else:
                n -= 1
                threading.Thread(target=self.record2).start()
                time.sleep(35)
        else:
            print(GPIO.input(sound2))

    def record(self):
        self.count += 1  # Increment the counter
        self.label_count.config(text="Number of times snoring: {}".format(self.count))
        proc = subprocess.Popen(['python','001.py'])
        
    def record2(self):
        self.count += 1  # Increment the counter
        self.label_count.config(text="Number of times snoring: {}".format(self.count))
        proc = subprocess.Popen(['python','002.py'])


root = tk.Tk()
app = VoiceRecorder(master=root)
GPIO.add_event_detect(sound, GPIO.BOTH, bouncetime=2)
GPIO.add_event_callback(sound, app.callback)
GPIO.add_event_detect(sound2, GPIO.BOTH, bouncetime=2)
GPIO.add_event_callback(sound2, app.callback2)
app.mainloop()

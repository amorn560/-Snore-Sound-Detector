from tkinter import *
import os
import pygame
import runpy
import subprocess
# pip install pillow
from PIL import Image, ImageTk



from tkinter import filedialog

class Window(Frame):
    def __init__(self, master=None):
        
        self.root = root
        self.root.title("Snoring Detector")
        # Window Geometry
        self.root.geometry("1000x600")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        
        
        trackframe = LabelFrame(self.root,text="WAV Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        trackframe.place(x=0,y=250,width=400,height=75)
        
        songtrack = Label(trackframe,textvariable=self.track,width=20,font=("times new roman",16,"bold"),bg="grey",fg="gold").grid(row=0,column=0,padx=10,pady=5)
        # Inserting Status Label
        trackstatus = Label(trackframe,textvariable=self.status,font=("times new roman",16,"bold"),bg="grey",fg="gold").grid(row=0,column=1,padx=10,pady=5)
        
        

        buttonframe = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        buttonframe.place(x=0,y=325,width=400,height=90)
    
        pngframe = LabelFrame(self.root,text="PNG View",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        pngframe.place(x=0,y=0,width=600,height=250)      

        recordframe = LabelFrame(self.root,text="Detect",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        recordframe.place(x=600,y=0,width=200,height=250)
        
        recordbtn = Button(recordframe,text="RECORD",command=self.record1,width=12,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=5,pady=5)
        #recordbtn = Button(recordframe,text="STOP",command='''self.open_img''',width=12,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=1,column=0,padx=5,pady=5)
                
        
        viewbtn = Button(buttonframe,text="VIEW GRAPH",command=self.open_img,width=10,height=1,font=("times new roman",10,"bold"),fg="navyblue",bg="gold").grid(row=0,column=0,padx=5,pady=5)
        
        playbtn = Button(buttonframe,text="PLAY",command=self.playsong,width=3,height=1,font=("times new roman",10,"bold"),fg="navyblue",bg="gold").grid(row=0,column=1,padx=5,pady=5)
        # Inserting Pause Button
        playbtn = Button(buttonframe,text="PAUSE",command=self.pausesong,width=5,height=1,font=("times new roman",10,"bold"),fg="navyblue",bg="gold").grid(row=0,column=2,padx=5,pady=5)
        # Inserting Unpause Button
        playbtn = Button(buttonframe,text="UNPAUSE",command=self.unpausesong,width=6,height=1,font=("times new roman",10,"bold"),fg="navyblue",bg="gold").grid(row=0,column=3,padx=5,pady=5)
        # Inserting Stop Button
        playbtn = Button(buttonframe,text="STOP",command=self.stopsong,width=4,height=1,font=("times new roman",10,"bold"),fg="navyblue",bg="gold").grid(row=0,column=4,padx=5,pady=5)
        
        
        # Creating Graph List Frame
        Graphframe = LabelFrame(self.root,text="Graph List",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        Graphframe.place(x=600,y=250,width=200,height=165)
        # Inserting scrollbar
        scrol_yy = Scrollbar(Graphframe,orient=VERTICAL)
        # Inserting Graph List listbox
        self.GraphList = Listbox(Graphframe,yscrollcommand=scrol_yy.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_yy.pack(side=RIGHT,fill=Y)
        scrol_yy.config(command=self.GraphList.yview)
        self.GraphList.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("/home/amorn560/Desktop/pro/MyPlots")

        # Fetching Songs with .png extension
        songtracks = [track for track in os.listdir() if track.endswith('.png')]

        # Inserting Songs into GraphList
        for track in songtracks:
            self.GraphList.insert(END, track)
       
          
        # Creating Playlist Frame
        songsframe = LabelFrame(self.root,text="Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
        songsframe.place(x=400,y=250,width=200,height=165)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe,orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(songsframe,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("/home/amorn560/Desktop/pro/MyPlots")

        # Fetching Songs with .wav extension
        songtracks = [track for track in os.listdir() if track.endswith('.wav')]

        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

          
          
          
          
          
        
     # Defining Play Song Function
     
     
    def record1(self):
        print('run to record')
        proc = subprocess.Popen(['python','re2.py'])
        #proc.wait()
        #proc.terminate()
        #runpy.run_path('re1.py')
     
     
     
    def playsong(self):
      # Displaying Selected Song title
      self.track.set(self.playlist.get(ACTIVE))
      # Displaying Status
      self.status.set("-Playing")
      # Loading Selected Song
      pygame.mixer.music.load(self.playlist.get(ACTIVE))
      # Playing Selected Song
      pygame.mixer.music.play()

    def stopsong(self):
      # Displaying Status
      self.status.set("-Stopped")
      # Stopped Song
      pygame.mixer.music.stop()

    def pausesong(self):
      # Displaying Status
      self.status.set("-Paused")
      # Paused Song
      pygame.mixer.music.pause()

    def unpausesong(self):
      # Displaying Status
      self.status.set("-Playing")
      # Playing back Song
      pygame.mixer.music.unpause() 

 
    def openfn(self):
        filename = self.GraphList.get(ACTIVE)
        return filename
    def open_img(self):
        x = self.openfn()
        img = Image.open(x)
        img = img.resize((550, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(root, image=img)
        panel.image = img
        panel.pack()
        panel.place(x=25,y=25,width=550,height=200)








# Creating TK Container
root = Tk()



# Passing Root to MusicPlayer Class
Window(root)
# Root Window Looping
root.mainloop()





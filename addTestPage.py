import os
import shutil
from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk
import cv2
from mutagen.mp3 import MP3
import pygame
import random

from animate import ProgressBarAnimator

class Page4(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="#111111")

        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        # Get screen width and height
        self.width = 1536
        self.height = 864
        
        self.songName = []
        self.songDuration = [] 
        self.songDiff = []
        self.songs = ""
        self.songs_path = ""
        
        # Create a label to display video preview
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        global frame
        frame = ctk.CTkFrame(master=self , bg_color="transparent", fg_color="#111111")
        frame.pack(fill="both", expand=True )
 
        inner1 = ctk.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent")      
        inner1.pack(side = "top",fill="both", expand=True )
        
        hidden = ctk.CTkLabel(master=inner1, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack( padx=50, side="top", anchor="nw")

        label = ctk.CTkLabel(master=inner1, text="Add Song", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#4CC9F0"))
        label.pack( padx=50, side="top", anchor="n")
        
        frame2 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        self.animator = ProgressBarAnimator(frame2)
        
        hidden1 = ctk.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        #Progession Label bar
        label1 = ctk.CTkButton(frame2, width=100,text='Frame Rate',   font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = ctk.CTkButton(frame2, width=100,text='Upload',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color='#262626',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = ctk.CTkButton(frame2, width=100,text='Cut time',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = ctk.CTkButton(frame2, width=100,text='Add song',     font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color="white",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = ctk.CTkButton(frame2, width=100,text='Export',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label1.place(x=5,y=60)
        label2.place(x=135,y=60)
        label3.place(x=250,y=60)
        label4.place(x=370,y=50)
        label5.place(x=495,y=60)
        
        infoText = ctk.CTkLabel(master=inner1, text="เลือกเพลงที่ต้องการใส่จากระบบแนะนำเพลง", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.16, rely = 0.25, anchor="n")

         #music recommendation frame
        global leftFrame
        leftFrame = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent")
        leftFrame.pack(pady=50 ,padx=(50,10), side="left",fill="both", expand=True ,anchor="nw")
        
        uploadFrame = ctk.CTkFrame(master=leftFrame, bg_color="transparent", fg_color="black", corner_radius = 5)
        uploadFrame.pack(pady=5 , side="top",fill="x" ,anchor="nw")
        
        uploadTitleText = ctk.CTkLabel(master=uploadFrame,text="Upload your song", font=("Tahoma", 25, "bold"), bg_color="transparent", fg_color="black", text_color=("#3A0CA3")) 
        uploadTitleText.pack(padx = 10,pady=(10,0), side="top", anchor="nw")
        
        # Upload button 
        self.uploadButton = ctk.CTkButton(master=uploadFrame, height= 70, text="Upload song", font=("Tahoma", 15, "bold"),text_color="#474747", corner_radius=1,border_width=1,border_color="#474747", fg_color="#202020", hover=False, command=self.select_song)
        self.uploadButton.pack(padx = 10,pady=10, side="top", fill="both", expand=True, anchor="nw")
        
        #show file name after user upload
        # self.filenamelabel = ctk.CTkLabel(self.uploadButton, text="", font=("Tahoma", 13, "bold"), bg_color="transparent", text_color="#474747",anchor="w",justify="left")
        # self.filenamelabel.grid(row=0, column=0, padx=10, pady=10)
        
        #line between Upload button and music recommendation 
        progressbar = ctk.CTkProgressBar(leftFrame, width=560,height= 5,fg_color="#262626",progress_color = "#FF0075",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 3,side="top", anchor="n")
        progressbar.set(1)
        
        musicFrame = ctk.CTkFrame(master=leftFrame, bg_color="transparent", fg_color="black", corner_radius = 5)
        musicFrame.pack(pady=5 , side="top",fill="x" ,anchor="nw")
        
        musicText = ctk.CTkLabel(master=musicFrame, text="Music Recommendation", font=("Tahoma", 25, "bold"), bg_color="transparent", fg_color="black", text_color=("#FF0075")) 
        musicText.pack(padx = 10,pady=(10,0), side="top", anchor="nw")
        
        musicinfoText = ctk.CTkLabel(master=musicFrame, text="The function is to have an AI predict the emotions of a character based on their facial expressions \nand then suggest music that suits the character's expression", font=("Tahoma", 10, "bold"), bg_color="transparent", fg_color="black", text_color=("#ffffff"),anchor="w",justify="left") 
        musicinfoText.pack(padx = 10, side="top", anchor="nw")
        
        #select song frame
        self.pickFrame = ctk.CTkFrame(master=leftFrame, bg_color="transparent", fg_color="black", corner_radius = 5)
        self.pickFrame.pack(pady=5 , side="top",fill="both", expand=True ,anchor="nw")
        
        # wait for ai to add text emotion
        musicText = ctk.CTkLabel(self.pickFrame, text="Here is a list of “Angry” ", font=("Tahoma", 25, "bold"), bg_color="transparent", fg_color="black", text_color=("#FF9029")) 
        musicText.pack(padx = 10,pady=(10,0), side="top", anchor="nw")
        
        # testsong
        self.folder_path = ["Angry",  "Sad", "Happy"]
        self.folder_path1 = ["Angry"]
        self.folder_path2 = ["Angry",  "Sad"]
        self.ramdom_songs(self.folder_path)
        
        
        #preview video
        global frame4
        frame4 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="#181818", corner_radius = 5,border_width=1,border_color="#474747")
        frame4.pack(pady=50 ,padx=(10,50), side="left",fill="both", expand=True ,anchor="nw")
        
        self.vdoPreview()

        nextButton = ctk.CTkButton(master=frame4, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,text_color="#4CC9F0",fg_color="#262626",hover_color="#253E46",command=lambda: controller.show_frame("Page5"))
        nextButton.place(relx=0.7, rely=0.85)
        

    def vdoPreview(self):
        aspect_ratio = 16/9
        frame_width = int(self.width * 0.55)
        frame_height = int(frame_width / aspect_ratio)
        self.vdoFrame = ctk.CTkFrame(frame4, width=frame_width, height=frame_height, fg_color="grey")
        self.vdoFrame.pack(pady = 10,side="top", anchor="n")

        self.cap = cv2.VideoCapture('./uploads/sample.mp4')
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            return

        self.frame_width = frame_width
        self.frame_height = frame_height

        self.label_img = ctk.CTkLabel(self.vdoFrame,text="")
        self.label_img.pack()

        self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.label_img.configure(image=img)
            self.label_img.image = img
            self.after(30, self.update_frame)
        else:
            print("Error: Frame not read.")
            self.cap.release()
            
    def add_image(self,image_path,x,y):
        image = Image.open(image_path)

        image = image.resize((x, y))
        image_tk = ImageTk.PhotoImage(image)
        return image_tk

    def start_animation(self):
        self.animator.animate_progressbar(start=0.5, target=0.7)

    def play_song(self, song_path):
        # ตรวจสอบว่าเพลงกำลังเล่นอยู่หรือไม่
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()  # หยุดเพลงถ้ากำลังเล่นอยู่
        else:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()  # เล่นเพลงถ้าไม่มีเพลงกำลังเล่น
            self.vdoFrame.destroy()
            self.vdoPreview()
            
    def ramdom_songs(self, folder_path):
        if len(folder_path) == 3:
            for i in folder_path: 
                self.read_song(i)
        elif len(folder_path) == 2:
            self.read_song(folder_path[0])
            self.read_song(folder_path[0])
            self.read_song(folder_path[1])
        elif len(folder_path) == 1:
            self.read_song(folder_path[0])
            self.read_song(folder_path[0])
            self.read_song(folder_path[0])
        else:
            print("No classify data")
        
        for i in self.songName:
            print(i)   
        for i in self.songDuration:
            print(i) 
        self.display_songs_button()
            
    def read_song(self, folder_path):
        songs = [f for f in os.listdir(f"./{folder_path}") if f.endswith('.mp3') and f not in self.songDiff]
        if len(songs) == 0:
            return
       
        random_song = random.sample(songs, min(len(songs), 1))[0]  # เลือกเพลงสุ่ม 1 เพลง
        song_name = random_song.split(".")[0]  # ตัดนามสกุลไฟล์ออก 
        file_ext = random_song.split(".")[1]
        # อ่านระยะเวลาของเพลง
        self.song_path = os.path.join(f"./{folder_path}",random_song)
        if file_ext == "mp3":
            audio = MP3(self.song_path)
        else:
            audio = None
        if audio:
            duration = int(audio.info.length)  # ระยะเวลาของเพลงเป็นวินาที
            minutes, seconds = divmod(duration, 60)
            duration_str = f"{minutes}:{seconds:02d}"  # รูปแบบ mm:ss
        else:
            duration_str = "Unknown"
        
        self.songName.append(song_name)
        self.songDuration.append(duration_str)
        self.songDiff.append(random_song)
        
    def display_songs_button(self):
        for i, song in enumerate(self.songName):
            # สร้างปุ่มสำหรับแต่ละเพลง
            framesong = ctk.CTkButton(
                self.pickFrame,
                text=f"Song {i+1} {self.folder_path[i]}: {self.songName[i]} {self.songDuration[i]}",
                font=("Tahoma", 18),
                bg_color="transparent",
                fg_color="#202020",
                anchor="w",
                command=lambda path=self.song_path: self.play_song(path)  # เรียกใช้ play_song เมื่อคลิกปุ่ม
            )
            framesong.pack(padx=10, pady=(5, 10), side="top", fill="both", expand=True, anchor="nw")
            
    def select_song(self):
        global filename
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select a song",
            filetypes=(("MP3 files", "*.mp3"), ("all files", "*.*"))
        )
        # upload to uploads folder
        if filename:
            # Define the destination folder (uploads)
            destination_folder = os.path.join(os.getcwd(), 'uploads_local_song')

            # Create the uploads folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Define the destination path for the file
            destination_path = os.path.join(destination_folder, os.path.basename(filename))

            # Copy the selected file to the uploads folder
            shutil.copy2(filename, destination_path)

            self.controller.songPaths.append(destination_path)  # Changed to songPaths

            print(f"Song file uploaded to: {destination_path}")
            self.list_song()  # Changed to list_song
        else:
            print("No file selected.")

    
    def list_song(self):
        for name in self.controller.songPaths:
            # self.filenamelabel.configure(text= name) 
            self.uploadButton.configure(text=name)    


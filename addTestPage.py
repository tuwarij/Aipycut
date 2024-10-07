import os
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
        global frame3
        frame3 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent")
        frame3.pack(pady=50 ,padx=(50,10), side="left",fill="both", expand=True ,anchor="nw")
        
        musicFrame = ctk.CTkFrame(master=frame3, bg_color="transparent", fg_color="black", corner_radius = 5)
        musicFrame.pack(pady=5 , side="top",fill="x" ,anchor="nw")
        
        musicText = ctk.CTkLabel(master=musicFrame, text="Music Recommendation", font=("Tahoma", 25, "bold"), bg_color="transparent", fg_color="black", text_color=("#FF0075")) 
        musicText.pack(padx = 10,pady=(10,0), side="top", anchor="nw")
        
        musicinfoText = ctk.CTkLabel(master=musicFrame, text="The function is to have an AI predict the emotions of a character based on their facial expressions \n and then suggest music that suits the character's expression", font=("Tahoma", 10, "bold"), bg_color="transparent", fg_color="black", text_color=("#ffffff"),anchor="w",justify="left") 
        musicinfoText.pack(padx = 10, side="top", anchor="nw")
        
        #line between music recommendation and pick song
        progressbar = ctk.CTkProgressBar(frame3, width=560,height= 5,fg_color="#262626",progress_color = "#FF0075",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 3,side="top", anchor="n")
        progressbar.set(1)
        
        #select song frame
        pickFrame = ctk.CTkFrame(master=frame3, bg_color="transparent", fg_color="black", corner_radius = 5)
        pickFrame.pack(pady=5 , side="top",fill="both", expand=True ,anchor="nw")
        
        musicText = ctk.CTkLabel(master=pickFrame, text="Here is a list of “Angry” ", font=("Tahoma", 25, "bold"), bg_color="transparent", fg_color="black", text_color=("#FF9029")) 
        musicText.pack(padx = 10,pady=(10,0), side="top", anchor="nw")
        
        folder_path = 'E:/!KMITL/3/AI/Aipycut/song_test'  # ใส่ path โฟลเดอร์ที่มีเพลง
        self.display_songs(pickFrame, folder_path)
        
        
        #preview video
        global frame4
        frame4 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="#181818", corner_radius = 5,border_width=1,border_color="#474747")
        frame4.pack(pady=50 ,padx=(10,50), side="left",fill="both", expand=True ,anchor="nw")
        
        self.vdoPreview()

        # Initialize components
        # self.addText()
        
        # # self.MuRecSide()
        # # self.vdoSide()
        # self.vdoPreview()
        
        # # self.buttonNext()
        # image_path = "circle.png"
        # image1 = self.add_image(image_path,250,200)
        # label_with_image = ctk.CTkLabel(frame3, width= 100,height=100,image=image1, text="",bg_color="black",corner_radius=5)
        # label_with_image.place(x=380, y=4)
        
        # image_path = "circle2.png"
        # image2 = self.add_image(image_path,200,130)
        # label_with_image = ctk.CTkLabel(frame3, width= 100,height=100,image=image2, text="",bg_color="black",corner_radius=5)
        # label_with_image.place(x=1, y=90)

        nextButton = ctk.CTkButton(master=frame4, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,text_color="#4CC9F0",fg_color="#262626",hover_color="#253E46",command=lambda: controller.show_frame("Page5"))
        nextButton.place(relx=0.7, rely=0.85)
        


    def addText(self):

        label_music_rec = ctk.CTkLabel(self, text="Music Recommend", font=("Tahoma", 32), text_color="#4CC9F0",bg_color="#181818")
        label_music_rec.place(relx=0.175, rely=0.275, anchor="nw")

    def MuRecSide(self):
        frame_width = int(self.width * 0.465)
        frame_height = int(self.height * 0.7)
        rec_frame = ctk.CTkFrame(self, width=frame_width, height=frame_height, fg_color="#0a0a0a")
        rec_frame.place(relx=0.025, rely=0.125, anchor="nw")

    def vdoSide(self):
        frame_width = int(self.width * 0.465)
        frame_height = int(self.height * 0.7)
        vdo_frame = ctk.CTkFrame(self, width=frame_width, height=frame_height, fg_color="#181818")
        vdo_frame.place(relx=0.51, rely=0.125, anchor="nw")

    def vdoPreview(self):
        aspect_ratio = 16/9
        frame_width = int(self.width * 0.55)
        frame_height = int(frame_width / aspect_ratio)
        vdoFrame = ctk.CTkFrame(frame4, width=frame_width, height=frame_height, fg_color="grey")
        vdoFrame.pack(pady = 10,side="top", anchor="n")

        self.cap = cv2.VideoCapture('./uploads/sample.mp4')
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            return

        self.frame_width = frame_width
        self.frame_height = frame_height

        self.label_img = ctk.CTkLabel(vdoFrame,text="")
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

    def display_songs(self, pickFrame, folder_path):
        # อ่านไฟล์ในโฟลเดอร์
        songs = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]  # เฉพาะไฟล์ที่เป็น .mp3 
        
        if len(songs) == 0:
            return  # หากไม่มีเพลงในโฟลเดอร์

        # เลือกเพลงแบบสุ่ม 3 เพลง
        random_songs = random.sample(songs, min(len(songs), 3))  # เลือกเพลงสุ่มสูงสุด 3 เพลง

        # สร้าง Label สำหรับแสดงชื่อเพลงและระยะเวลา
        for i, song in enumerate(random_songs):
            # ตัดนามสกุลไฟล์ออก
            song_name, file_ext = os.path.splitext(song)

            # อ่านระยะเวลาของเพลง
            song_path = os.path.join(folder_path, song)
            if file_ext == ".mp3":
                audio = MP3(song_path)
            else:
                audio = None

            if audio:
                duration = int(audio.info.length)  # ระยะเวลาของเพลงเป็นวินาที
                minutes, seconds = divmod(duration, 60)
                duration_str = f"{minutes}:{seconds:02d}"  # รูปแบบ mm:ss
            else:
                duration_str = "Unknown"

            # สร้างปุ่มสำหรับแต่ละเพลง
            framesong = ctk.CTkButton(
                master=pickFrame,
                text=f"Song {i+1}: {song_name} {duration_str}",
                font=("Tahoma", 20),
                bg_color="transparent",
                fg_color="#202020",
                anchor="w",
                command=lambda path=song_path: self.play_song(path)  # เรียกใช้ play_song เมื่อคลิกปุ่ม
            )
            framesong.pack(padx=10, pady=(5, 10), side="top", fill="both", expand=True, anchor="nw")    


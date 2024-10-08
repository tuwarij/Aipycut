import os
import cv2
import shutil
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

from animate import ProgressBarAnimator

class Page5(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        
        self.width = 1536
        self.height = 864

        self.frame = ctk.CTkFrame(master=self, bg_color="transparent", fg_color="#111111")
        self.frame.pack(fill="both", expand=True)

        hidden = ctk.CTkLabel(self.frame, text="", bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack(side="top", anchor="n")

        text = ctk.CTkLabel(self.frame, text="Final", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color="#4CC9F0")
        text.pack(side="top", anchor="n")
        
        frame2 = ctk.CTkFrame(self.frame, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        self.animator = ProgressBarAnimator(frame2)
        
        hidden1 = ctk.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        label1 = ctk.CTkButton(frame2, width=100,text='Frame Rate', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = ctk.CTkButton(frame2, width=100,text='Upload', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = ctk.CTkButton(frame2, width=100,text='Cut time', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = ctk.CTkButton(frame2, width=100,text='Add song', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = ctk.CTkButton(frame2, width=100,text='Export', font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color='white',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        
        label1.place(x=5,y=60)
        label2.place(x=135,y=60)
        label3.place(x=250,y=60)
        label4.place(x=370,y=60)
        label5.place(x=495,y=50)

        infoText = ctk.CTkLabel(self.frame, text="ตัวอย่าง วิดีโอ สามารถกดปุ่ม export เพื่อโหลดไฟล์ได้", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.34, rely = 0.25, anchor="n")
        
        monitor = ctk.CTkLabel(self.frame, text="", fg_color="#181818")
        monitor.pack(padx=250, pady=50, side="top", anchor="n", fill="both", expand=True)
        
        
        self.preview = ctk.CTkLabel(master=monitor,text="", fg_color="#181818",bg_color="#181818")
        self.preview.place(x=0, y=0,anchor="nw")
        
        self.video_Preview()

        self.exportButton = ctk.CTkButton(master=monitor, width=150, height=50, text="Export", font=("Tahoma", 15, "bold"),corner_radius = 1,text_color="#4CC9F0",fg_color="#262626",hover_color="#253E46", command=self.select_export_directory)
        self.exportButton.place(relx=0.75,rely=0.8)
        self.exportButton.lift()

    def select_export_directory(self):
        file_path = self.controller.export_path

        # upload to uploads folder
        dest_folder = filedialog.askdirectory(title="Select the destination folder")

        if not dest_folder:
            return

        try:
            # Move the file
            shutil.copy2(file_path, dest_folder)
            print(f"Success\n"+ f"File moved to {dest_folder}")
        except Exception as e:
            print(f"Error{e}")

        quit()

    def start_animation(self):
        self.animator.animate_progressbar(start=0.7, target=1)
        
    def video_Preview(self):
        aspect_ratio = 16/9
        self.frame_width = int(self.width*0.65)
        self.frame_height = int(self.frame_width / aspect_ratio)
        self.cap = cv2.VideoCapture(self.controller.export_path)
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            return
        self.update_frame()
        
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (self.frame_width, self.frame_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            self.preview.configure(image=img)
            self.preview.image = img
            self.after(30, self.update_frame)
        else:
            print("Error: Frame not read.")
            self.cap.release()
        
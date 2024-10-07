import os
import cv2
import customtkinter
from PIL import Image, ImageTk
from tkinter import filedialog

from animate import ProgressBarAnimator

customtkinter.set_appearance_mode("dark")

def select_video():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select a video",
        filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*"))
    )
    if filename:
        play_video(filename)  # Call play_video after selecting a file

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    def update_frame():
        ret, frame = cap.read()
        if ret:
            # Convert the frame to an image for displaying in tkinter
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)

            # Update the label with the new frame
            preview.configure(image=imgtk)
            preview.image = imgtk

            # Call this function again after 10ms to continue the video
            preview.after(10, update_frame)
        else:
            cap.release()  # Release the video when it's done

    update_frame()  # Start the video loop

class Page5(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        frame = customtkinter.CTkFrame(master=self, bg_color="transparent", fg_color="#111111")
        frame.pack(fill="both", expand=True)

        hidden = customtkinter.CTkLabel(master=frame, text="", bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack(side="top", anchor="n")

        text = customtkinter.CTkLabel(master=frame, text="Final", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color="#4CC9F0")
        text.pack(side="top", anchor="n")
        
        frame2 = customtkinter.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        self.animator = ProgressBarAnimator(frame2)
        
        hidden1 = customtkinter.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        label1 = customtkinter.CTkButton(frame2, width=100,text='Frame Rate', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = customtkinter.CTkButton(frame2, width=100,text='Upload', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = customtkinter.CTkButton(frame2, width=100,text='Cut time', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = customtkinter.CTkButton(frame2, width=100,text='Add song', font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = customtkinter.CTkButton(frame2, width=100,text='Export', font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color='white',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        
        label1.place(x=5,y=60)
        label2.place(x=135,y=60)
        label3.place(x=250,y=60)
        label4.place(x=370,y=60)
        label5.place(x=495,y=50)

        infoText = customtkinter.CTkLabel(master=frame, text="ตัวอย่าง วิดีโอ สามารถกดปุ่ม export เพื่อโหลดไฟล์ได้", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.34, rely = 0.25, anchor="n")
        
        monitor = customtkinter.CTkLabel(master=frame, text="", fg_color="#181818")
        monitor.pack(padx=250, pady=50, side="top", anchor="n", fill="both", expand=True)
        
        global preview
        preview = customtkinter.CTkLabel(master=monitor,text="", fg_color="#181818",bg_color="#181818")
        preview.place(x=0, y=0)

        # uploadButton = customtkinter.CTkButton(master=frame, width=150, height=50, text="Upload", font=("Tahoma", 15, "bold"), corner_radius=1, border_width=1, border_color="#4CC9F0", fg_color="#262626", hover_color="#4CC9F0", command=select_video)
        # uploadButton.place(x=1100, y=670)

        exportButton = customtkinter.CTkButton(master=monitor, width=150, height=50, text="Export", font=("Tahoma", 15, "bold"),corner_radius = 1,text_color="#4CC9F0",fg_color="#262626",hover_color="#253E46", command=lambda: controller.show_frame("Page1"))
        exportButton.place(relx=0.75,rely=0.8)
        
    def start_animation(self):
        self.animator.animate_progressbar(start=0.7, target=1)

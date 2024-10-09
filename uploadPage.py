import os
import shutil
import VideoEditor
import customtkinter
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2  # Import OpenCV to extract video frames
from animate import ProgressBarAnimator

customtkinter.set_appearance_mode("dark")

class Page2(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)
        self.controller = controller

        frame = customtkinter.CTkFrame(master=self , bg_color="transparent", fg_color="#111111")
        frame.pack(fill="both", expand=True )

        hidden = customtkinter.CTkLabel(master=frame, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack( side="top", anchor="n")

        #Topic text
        text = customtkinter.CTkLabel(master=frame, text="Upload video", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#4CC9F0"))
        text.pack( side = "top", anchor="n")
        
        frame2 = customtkinter.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        self.animator = ProgressBarAnimator(frame2)
        
        hidden1 = customtkinter.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        #Progressive Label bar
        label1 = customtkinter.CTkButton(frame2, width=100,text='Frame Rate',   font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = customtkinter.CTkButton(frame2, width=100,text='Upload',       font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color='white',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = customtkinter.CTkButton(frame2, width=100,text='Cut time',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = customtkinter.CTkButton(frame2, width=100,text='Add song',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = customtkinter.CTkButton(frame2, width=100,text='Export',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label1.place(x=5,y=60)
        label2.place(x=135,y=50)
        label3.place(x=250,y=60)
        label4.place(x=370,y=60)
        label5.place(x=495,y=60)
        
        infoText = customtkinter.CTkLabel(master=frame, text="อัพโหลดคลิปที่ต้องการแก้ไขที่ช่องอัพโหลด", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.31, rely = 0.25, anchor="n")

        # Upload button with image placeholder
        self.uploadButton = customtkinter.CTkButton(master=frame, width=900, height=500, text="Upload video", font=("Tahoma", 20, "bold"), corner_radius=1, border_width=2, border_color="#474747", fg_color="#181818", hover=False, command=self.select_video)
        self.uploadButton.pack(pady=50, padx=250, side="top", fill="both", expand=True, anchor="nw")
        
        self.filenamelabel = customtkinter.CTkLabel(self.uploadButton, text="", font=("Tahoma", 15, "bold"), bg_color="transparent", text_color="#8c8c8c",anchor="w",justify="left")
        self.filenamelabel.grid(row=0, column=0, padx=10, pady=10)
        
        # Next button
        nextButton = customtkinter.CTkButton(master=self.uploadButton, width=150, height=50, text="Next", font=("Tahoma", 15, "bold"), corner_radius=1, text_color="#4CC9F0", fg_color="#262626", hover_color="#253E46", command=lambda: controller.show_frame("Page3"))
        nextButton.place(relx=0.75, rely=0.8)

        #Next button
        nextButton = customtkinter.CTkButton(self.uploadButton, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,text_color="#4CC9F0",fg_color="#262626",hover_color="#253E46",command=lambda: controller.show_frame("Page3"))
        nextButton.place(relx=0.75,rely=0.8) 
           
        
    def select_video(self):
        global filename
        filename = filedialog.askopenfilename(
            title="Select a video",
            filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*"))
        )
        # upload to uploads folder
        if filename:
            # Define the destination folder (uploads)
            destination_folder = os.path.join(os.getcwd(), 'uploads')
            
            # Create the uploads folder if it doesn't exist
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            
            # Define the destination path for the file
            destination_path = os.path.join(destination_folder, os.path.basename(filename))
            
            # Copy the selected file to the uploads folder
            shutil.copy2(filename, destination_path)

            self.controller.videoPaths.append(destination_path)
            
            print(f"Video file uploaded to: {destination_path}")
            self.list_video()
        else:
            print("No file selected.")
    
    def list_video(self):
        strName = ""
        for name in self.controller.videoPaths:
            strName = strName + name + "\n"+"\n"+" "
            self.filenamelabel.configure(text=f"File selected : \n {strName}") 
            self.uploadButton.configure(text="")
            

    def start_animation(self):
        self.animator.animate_progressbar(start=0.1, target=0.3)

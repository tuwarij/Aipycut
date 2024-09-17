import os
import customtkinter
from PIL import Image, ImageDraw, ImageTk
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")

def select_video():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select a video",
        filetypes=(("MP4 files", "*.mp4"), ("all files", "*.*"))
    )
    print(filename)

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
        
        #Progression Bar
        progressbar = customtkinter.CTkProgressBar(frame2, width=600,height= 20,fg_color="#262626",progress_color = "#4CC9F0",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 20,side="top", anchor="n")
        progressbar.set(0.40)
        
        hidden1 = customtkinter.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        #Prgessive Label bar
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

        #Upload button
        uploadButton = customtkinter.CTkButton(master=frame, width= 150,height=50,text="Upload your video", font=("Tahoma", 20,"bold"),text_color = "#8c8c8c",corner_radius = 1,border_width=2,border_color="#474747",fg_color="#262626",hover = False,command=select_video)
        uploadButton.pack(pady=50 ,padx=250, side="top",fill="both", expand=True ,anchor="nw")

        #Next button
        nextButton = customtkinter.CTkButton(master=self, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,border_width=1,border_color="#4CC9F0",fg_color="#262626",hover_color="#4CC9F0",command=lambda: controller.show_frame("Page3"))
        nextButton.place(x=1080,y=640)    
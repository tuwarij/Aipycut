import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

ctk.set_appearance_mode("dark")

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
    
        frame = ctk.CTkFrame(master=self , bg_color="transparent", fg_color="#111111")
        frame.pack(fill="both", expand=True )
 
        inner1 = ctk.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent")      
        inner1.pack(side = "top",fill="both", expand=True )
        
        hidden = ctk.CTkLabel(master=inner1, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack( padx=50, side="top", anchor="nw")

        label = ctk.CTkLabel(master=inner1, text="Cut Time", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#4CC9F0"))
        label.pack( padx=50, side="top", anchor="n")
        
        frame2 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent")
        frame2.pack( side = "top")
        
        #Progression bar
        progressbar = ctk.CTkProgressBar(frame2, width=600,height= 20,fg_color="#262626",progress_color = "#4CC9F0",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 20,side="top", anchor="n")
        progressbar.set(0.60)
        
        hidden1 = ctk.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden1.pack( side="top", anchor="n")
        
        #Progession Label bar
        label1 = ctk.CTkButton(frame2, width=100,text='Frame Rate',   font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label2 = ctk.CTkButton(frame2, width=100,text='Upload',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color='#262626',corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label3 = ctk.CTkButton(frame2, width=100,text='Cut time',     font=("Tahoma", 15, "bold"),text_color = "#4CC9F0", fg_color="white",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label4 = ctk.CTkButton(frame2, width=100,text='Add song',     font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label5 = ctk.CTkButton(frame2, width=100,text='Export',       font=("Tahoma", 15, "bold"),text_color = "#8c8c8c", fg_color="#262626",corner_radius = 50,border_width=2,border_color="#474747",hover = False)
        label1.place(x=5,y=60)
        label2.place(x=135,y=60)
        label3.place(x=250,y=50)
        label4.place(x=370,y=60)
        label5.place(x=495,y=60)

        label2 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="#181818", corner_radius = 5,border_width=1,border_color="#474747")
        label2.pack(pady=50 ,padx=250, side="top",fill="both", expand=True ,anchor="nw")

        nextButton = ctk.CTkButton(master=self, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,border_width=1,border_color="#4CC9F0",fg_color="#262626",hover_color="#4CC9F0",command=lambda: controller.show_frame("Page4"))
        nextButton.place(x=1080,y=640)

        
        # Time entry fields
        self.timeEndStartFields()


    def cutText(self):
        label = ctk.CTkLabel(self, text="Cut Length Video", font=("Tahoma", 32,"bold"), text_color="#4CC9F0")
        label.place(relx=0.5, rely=0.07, anchor="center")

    def bgField(self):
        # Field for video frame display or editing area
        frame_width = 0.95
        frame_height = 0.7
        cutFrame = ctk.CTkFrame(self, width=frame_width, height=frame_height, fg_color="#181818")
        cutFrame.place(relx=0.025, rely=0.125)

    def progressBar(self):
        # Step progress bar similar to the other pages
        label1 = ctk.CTkButton(self, width=100, text='Frame Rate', font=("Tahoma", 15, "bold"), text_color="#8c8c8c", fg_color="#262626", corner_radius=50, border_width=2, border_color="#474747", hover=False)
        label2 = ctk.CTkButton(self, width=100, text='Upload', font=("Tahoma", 15, "bold"), text_color="#4CC9F0", fg_color='white', corner_radius=50, border_width=2, border_color="#474747", hover=False)
        label3 = ctk.CTkButton(self, width=100, text='Cut time', font=("Tahoma", 15, "bold"), text_color="#8c8c8c", fg_color="#262626", corner_radius=50, border_width=2, border_color="#474747", hover=False)
        label4 = ctk.CTkButton(self, width=100, text='Add song', font=("Tahoma", 15, "bold"), text_color="#8c8c8c", fg_color="#262626", corner_radius=50, border_width=2, border_color="#474747", hover=False)
        label5 = ctk.CTkButton(self, width=100, text='Export', font=("Tahoma", 15, "bold"), text_color="#8c8c8c", fg_color="#262626", corner_radius=50, border_width=2, border_color="#474747", hover=False)
        
        label1.place(x=5, y=60)
        label2.place(x=135, y=50)
        label3.place(x=250, y=60)
        label4.place(x=370, y=60)
        label5.place(x=495, y=60)

    def timeEndStartFields(self):
    # Number of video fields
        numOfvideos = 4
        
        for i in range(numOfvideos):
            offset = 0.2 + (0.185 * i)  # Adjust spacing as needed

            # Start Time Label
            labelStart = ctk.CTkLabel(
                self,
                text="Start Time :",
                font=("Tahoma", 16),
                text_color="white",
                bg_color="#181818"
            )
            labelStart.place(relx=offset, rely=0.65)

            # Start Time Entry
            start_time_entry = ctk.CTkEntry(
                self,
                font=("Tahoma", 14),
                width=100
            )
            start_time_entry.place(relx=offset + 0.07, rely=0.65)

            # End Time Label
            labelEnd = ctk.CTkLabel(
                self,
                text="End Time :",
                font=("Tahoma", 16),
                text_color="white",
                bg_color="#181818"
            )
            labelEnd.place(relx=offset, rely=0.7)

            # End Time Entry
            end_time_entry = ctk.CTkEntry(
                self,
                font=("Tahoma", 14),
                width=100
            )
            end_time_entry.place(relx=offset + 0.07, rely=0.7)
            self.vdoPreview(offset)

    def vdoPreview(self,x):
        #1536x864
        aspect_ratio = 5 / 4
        frame_width = int(1536 * 0.35*0.6)
        frame_height = int(frame_width / aspect_ratio)
        vdoFrame = ctk.CTkFrame(self, width=frame_width, height=frame_height, fg_color="grey")
        vdoFrame.place(relx=x, rely=0.3, anchor="nw")

        self.cap = cv2.VideoCapture('test.mp4')
        if not self.cap.isOpened():
            print("Error: Unable to open video file.")
            return

        self.frame_width = frame_width
        self.frame_height = frame_height

        self.label_img = ctk.CTkLabel(vdoFrame)
        self.label_img.pack(expand=True, fill="both")
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

    



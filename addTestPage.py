import customtkinter as ctk
from PIL import Image, ImageTk
import cv2

class Page4(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="#111111")

        # Get screen width and height
        self.width = 1536
        self.height = 864
        
        # Create a label to display video preview
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
    
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
        
        #Progression bar
        progressbar = ctk.CTkProgressBar(frame2, width=600,height= 20,fg_color="#262626",progress_color = "#4CC9F0",orientation="horizontal",corner_radius=10)
        progressbar.pack( pady = 20,side="top", anchor="n")
        progressbar.set(0.80)
        
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

        label2 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="#181818", corner_radius = 5,border_width=1,border_color="#474747")
        label2.pack(pady=50 ,padx=250, side="top",fill="both", expand=True ,anchor="nw")

        # Initialize components
        self.addText()
        # self.MuRecSide()
        # self.vdoSide()
        self.vdoPreview()
        # self.buttonNext()

        nextButton = ctk.CTkButton(master=self, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,border_width=1,border_color="#4CC9F0",fg_color="#262626",hover_color="#4CC9F0",command=lambda: controller.show_frame("Page5"))
        nextButton.place(x=1080,y=640)


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
        aspect_ratio = 5 / 4
        frame_width = int(self.width * 0.35)
        frame_height = int(frame_width / aspect_ratio)
        vdoFrame = ctk.CTkFrame(self, width=frame_width, height=frame_height, fg_color="grey")
        vdoFrame.place(relx=0.525, rely=0.3, anchor="nw")

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


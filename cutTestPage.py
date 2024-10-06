import customtkinter as ctk
from animate import ProgressBarAnimator
from PIL import Image, ImageTk
from AI.srcs.emotion_detector import emotion_detection
import cv2

ctk.set_appearance_mode("dark")

class Page3(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.video_timings = []
        # Page Bg
        frame = ctk.CTkFrame(master=self , bg_color="transparent", fg_color="#111111")#111111
        frame.pack(fill="both", expand=True )

        # Inner Frame in Page bg (for what??)
        inner1 = ctk.CTkFrame(master=frame, bg_color="transparent", fg_color="transparent") #transparent
        inner1.pack(side = "top",fill="both", expand=True )

        # for make margin on the top
        hidden = ctk.CTkLabel(master=inner1, text="" ,bg_color="transparent", fg_color="transparent", text_color="black")
        hidden.pack( padx=50, side="top", anchor="nw")

        # Page Label
        label = ctk.CTkLabel(master=inner1, text="Cut Time", font=("Tahoma", 30, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#4CC9F0"))
        label.pack( padx=50, side="top", anchor="n")

        # frame for progress bar
        frame2 = ctk.CTkFrame(master=inner1, bg_color="transparent", fg_color="transparent") #transparent
        frame2.pack( side = "top")

        self.animator = ProgressBarAnimator(frame2)

        # for show progress bar
        hidden1 = ctk.CTkLabel(master=frame2, text="" ,bg_color="transparent", fg_color="transparent", text_color="black") #
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
        
        infoText = ctk.CTkLabel(master=frame, text="กำหนดช่วงเวลาที่ต้องการจะตัดในแต่ละคลิป", font=("Tahoma", 15, "bold"), bg_color="transparent", fg_color="transparent", text_color=("#8c8c8c"))
        infoText.place(relx = 0.31, rely = 0.243, anchor="n")

        # frame inner for conntent
        scrollFrame = ctk.CTkScrollableFrame(master=inner1, orientation="horizontal", bg_color="transparent", fg_color="#181818", corner_radius=5, border_width=1, border_color="#474747")
        scrollFrame.pack(pady=50, padx=250, side="top", fill="both", expand=True, anchor="nw")

        for i in range(len(controller.videoPaths)):
            col_offset = 2 * i  # Ensures label and entry for each video are in separate columns

            # Video Preview Frame
            aspect_ratio = 5 / 4
            frame_width = int(1536 * 0.35 * 0.6)
            frame_height = int(frame_width / aspect_ratio)
            vdoFrame = ctk.CTkFrame(scrollFrame, width=frame_width, height=frame_height, fg_color="grey")
            vdoFrame.grid(row=0, column=col_offset, columnspan=2, padx=30, pady=(10, 0))  # Video preview spans two columns

            self.cap = cv2.VideoCapture(controller.videoPaths[i])
            if not self.cap.isOpened():
                print(f"Error: Unable to open video file {controller.videoPaths[i]}")
                return

            self.frame_width = frame_width
            self.frame_height = frame_height

            self.label_img = ctk.CTkLabel(vdoFrame,text="")
            self.label_img.pack(expand=True, fill="both")
            self.update_frame()

            # Start Time Label and Entry
            labelStart = ctk.CTkLabel(scrollFrame, text="Start Time:", font=("Tahoma", 16), text_color="white", bg_color="#181818")
            labelStart.grid(row=1, column=col_offset, padx=(30, 0), pady=(10, 0), sticky="w")  # Label in its own column
            start_time_entry = ctk.CTkEntry(scrollFrame, font=("Tahoma", 14), width=100)
            start_time_entry.grid(row=1, column=col_offset + 1, padx=(0, 30), pady=(10, 0))  # Entry in next column

            # End Time Label and Entry
            labelEnd = ctk.CTkLabel(scrollFrame, text="End Time:", font=("Tahoma", 16), text_color="white", bg_color="#181818")
            labelEnd.grid(row=2, column=col_offset, padx=(30, 0), pady=(10, 0), sticky="w")  # Label in its own column
            end_time_entry = ctk.CTkEntry(scrollFrame, font=("Tahoma", 14), width=100)
            end_time_entry.grid(row=2, column=col_offset + 1, padx=(0, 30), pady=(10, 0))  # Entry in next column

            self.video_timings.append({'start_entry': start_time_entry, 'end_entry': end_time_entry})

        nextButton = ctk.CTkButton(master=self, width= 150,height=50,text="Next", font=("Tahoma", 15,"bold"),corner_radius = 1,border_width=1,border_color="#4CC9F0",fg_color="#262626",hover_color="#4CC9F0",command=lambda: [self.collect_data(), controller.show_frame("Page4")])
        nextButton.place(x=1080,y=640)

    def collect_data(self):
        for index, timing in enumerate(self.video_timings):
            self.controller.video_editor.open_video(self.controller.videoPaths[index])
            if timing['start_entry'].get():
                start_time = timing['start_entry'].get()
                self.controller.video_editor.set_start(start_time)
                print(f"Video {index + 1}: Start Time = {start_time}", end=", ")
            if timing['end_entry'].get():
                end_time = timing['end_entry'].get()
                self.controller.video_editor.set_end(end_time)
                print(f"End Time = {end_time}")
            self.controller.video_editor.cut_clip()
            self.controller.video_editor.add_to_timeline()
        self.controller.video_editor.merge_clips()

        video_path = "./uploads/sample.mp4"
        self.controller.video_editor.export_video(video_path)

        self.controller.emotions = emotion_detection(video_path)
        print("Emotions detected:", self.controller.emotions)

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

    def start_animation(self):
        self.animator.animate_progressbar(start=0.3, target=0.5)

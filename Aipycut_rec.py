import tkinter as tk
from tkinter import Button, Canvas, Frame, Label
from PIL import Image, ImageTk
import cv2

def recMainWindow(recWindow):
    recWindow.title("Aipycut")
    width = recWindow.winfo_screenwidth() 
    height = recWindow.winfo_screenheight()
    recWindow.configure(bg="#111111")

    
    recWindow.geometry("%dx%d" % (width, height))
    
    # Clear existing widgets
    for widget in recWindow.winfo_children():
        widget.destroy()

    
    MuRecSide(recWindow, width, height)
    vdoSide(recWindow, width, height)
    vdoPreview(recWindow, width, height)
    buttonNext(recWindow, width, height)
    addText(recWindow, width, height)
   

def addText(recWindow, width, height):
    labeladdSong = Label(recWindow, text="Add song", font=("IBM Plex Sans Thai", 32), fg="#4CC9F0", bg="#111111")
    labeladdSong.place(relx=0.51, rely=0.05, anchor="nw")
    labelMusicRec = Label(recWindow, text="Music Recommend", font=("IBM Plex Sans Thai", 32), fg="#4CC9F0", bg="#0a0a0a")
    labelMusicRec.place(relx=0.03, rely=0.13, anchor="nw")

    

def MuRecSide(recWindow, width, height):
    frame_width = int(width * 0.465)  
    frame_height = int(height * 0.7)
    recFrame = Frame(recWindow, width=frame_width, height=frame_height, bg="#0a0a0a")
    recFrame.place(relx=0.025, rely=0.125, anchor="nw")

def vdoSide(recWindow, width, height):
    frame_width = int(width * 0.465)
    frame_height = int(height * 0.7)
    vdoFrame = Frame(recWindow, width=frame_width, height=frame_height, bg="#181818")
    vdoFrame.place(relx=0.51, rely=0.125, anchor="nw")

def vdoPreview(recWindow, width, height):
    frame_width = int(width * 0.425)
    frame_height = int(height * 0.575)
    vdoFrame = Frame(recWindow, width=frame_width, height=frame_height, bg="grey")
    vdoFrame.place(relx=0.53, rely=0.165, anchor="nw")

    cap = cv2.VideoCapture('test.mp4')
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    def update_frame():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (frame_width, frame_height))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(img)
            label_img.config(image=img)
            label_img.image = img
            recWindow.after(30, update_frame)
        else:
            cap.release()

    label_img = Label(vdoFrame)
    label_img.pack(expand=True, fill="both")
    update_frame()

def buttonNext(recWindow, width, height):
    button_frame = Frame(recWindow, bg="#4CC9F0", padx=1, pady=1) 
    button_frame.place(relx=0.928, rely=0.835, anchor="center")

    btn = Button(button_frame, text='Next', command=recWindow.destroy, fg='white', bg="#262626",activebackground='#0d0d0d',activeforeground='white')
    btn.config(width=11, height=1) 
    btn.pack()

def main(recWindow):
    recMainWindow(recWindow)

# recWindow = tk.Tk()
# main(recWindow)
# recWindow.mainloop()
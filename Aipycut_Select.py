import tkinter as tk
from tkinter import Button, Entry, Frame, Label, Canvas, Scrollbar
from tkinter import ttk
import Aipycut_rec as airec

def selectMainWindow():
    selectWindow = tk.Tk()
    selectWindow.title("Aipycut")
    width = selectWindow.winfo_screenwidth() 
    height = selectWindow.winfo_screenheight()
    selectWindow.configure(bg="#111111")
    selectWindow.state('zoomed')

    selectText(selectWindow, width, height)
    bgFeild(selectWindow, width, height) 
    
    sildeZone(selectWindow, width, height)

    # vdoField(selectWindow, width, height)
    # timeEndStartFiled(selectWindow, width, height)
    buttonNext(selectWindow, width, height)
    selectWindow.mainloop()

def selectText(selectWindow, width, height):
    label = Label(selectWindow, text="Select Length Video", font=("IBM Plex Sans Thai", 32), fg="#4CC9F0", bg="#111111")
    label.place(relx=0.5, rely=0.07, anchor="center")


def bgFeild(selectWindow, width, height):
    frame_width = int(width * 0.95)  
    frame_height = int(height * 0.7)
    selectFrame = Frame(selectWindow, width=frame_width, height=frame_height, bg="#181818")
    selectFrame.place(relx=0.025, rely=0.125 )


def buttonNext(selectWindow, width, height):
    button_frame = Frame(selectWindow, bg="#4CC9F0", padx=1, pady=1) 
    button_frame.place(relx=0.928, rely=0.835, anchor="center")  
    
    btn = Button(button_frame, text='Next', command=lambda: nextWindow(selectWindow), fg='white', bg="#262626",activebackground='#0d0d0d',activeforeground='white')
    btn.config(width=11, height=1) 
    btn.pack()

def vdoField(selectWindow,width,height):
    frame_width = int(width * 0.2)  
    frame_height = int(height * 0.35)
    vdoFrame = Frame(selectWindow, width=frame_width, height=frame_height, bg="#474747")
    vdoFrame.place(relx=0.1, rely=0.2)

def timeEndStartFiled(selectWindow, width, height):

    labelStart = Label(selectWindow, text="Start Time :", font=("IBM Plex Sans Thai", 16), fg="white", bg="#474747")
    labelStart.place(relx=0.1, rely=0.575)

    start_time_entry = Entry(selectWindow, font=("IBM Plex Sans Thai", 14), width=10)
    start_time_entry.place(relx=0.18, rely=0.575) 

    labelEnd = Label(selectWindow, text="End Time   :", font=("IBM Plex Sans Thai", 16), fg="white", bg="#474747")
    labelEnd.place(relx=0.1, rely=0.625)

    end_time_entry = Entry(selectWindow, font=("IBM Plex Sans Thai", 14), width=10)
    end_time_entry.place(relx=0.18, rely=0.625) 

def sildeZone(selectWindow, width, height):
    # canvas = Canvas(selectWindow, bg="#111111", width=int(width * 0.9065), height=int(height * 0.575),highlightthickness=0, bd=0)  # Remove the border and highlight
    # canvas.place(relx=0.05, rely=0.165)
    # h_scrollbar = Scrollbar(selectWindow, orient="horizontal", command=canvas.xview)
    # h_scrollbar.pack(side="bottom", fill="x")
    # scrollFrame = selectWindow.CTk

    vdoField(selectWindow,width,height)
    timeEndStartFiled(selectWindow, width, height)

def nextWindow(selectWindow):
    airec.main(selectWindow)


selectMainWindow()

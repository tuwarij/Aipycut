# app.py
import VideoEditor
import customtkinter as ctk
from FirstPage import Page1
from uploadPage import Page2
from finalPage import Page5
from cutTestPage import Page3
from addTestPage import Page4

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Aipycut")
        self.geometry("1280x720")

        self.frames = {}

        self.video_editor = None
        self.videoPaths = []
        self.emotions = []
        self.songPaths = []
        self.export_path = None
        
        # Container to hold all pages
        self.container = ctk.CTkFrame(self, fg_color="black")
        self.container.pack(fill="both", expand=True)
        self.frame = None
        
        # Start with Page1
        self.show_frame("Page1")

    def show_frame(self, page_name):

        if self.frame:
            self.frame.destroy()

        for F in (Page1, Page2, Page3, Page4, Page5):
            if page_name == F.__name__:
                self.frame = F(parent=self.container, controller=self)
                self.frame.place(x=0, y=0, relwidth=1, relheight=1)
                self.frame.start_animation()

if __name__ == "__main__":
    app = App()
    app.mainloop()
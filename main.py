# app.py
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
        self.geometry("1536x864")
        self.after(0, lambda:self.state('zoomed'))

        self.frames = {}
        
        # Container to hold all pages
        container = ctk.CTkFrame(self, fg_color="black")
        container.pack(fill="both", expand=True)

        # Add both pages to the container
        for F in (Page1, Page2,Page3, Page4,Page5):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Start with Page1
        self.show_frame("Page1")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # Bring the frame to the front

if __name__ == "__main__":
    app = App()
    app.mainloop()

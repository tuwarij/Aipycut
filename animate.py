import customtkinter

class ProgressBarAnimator:
    def __init__(self, parent_frame):
        # Create the progress bar in the given parent frame
        self.progressbar = customtkinter.CTkProgressBar(parent_frame, width=600, height=20, fg_color="#262626", 
                                                        progress_color="#4CC9F0", orientation="horizontal", 
                                                        corner_radius=10)
        self.progressbar.pack(pady=20, side="top", anchor="n")
        self.progressbar.set(0)  # Initialize the progress bar at 0

    def animate_progressbar(self, start=0, target=0.1, increment=0.03, delay=50):
        self.progress = start  # Start from the specified start value
        self.progressbar.set(self.progress)  # Initialize the progress bar to the start value

        def update():
            if self.progress <= target:  # Animate until it reaches the target value
                self.progressbar.set(self.progress)
                self.progress += increment
                self.progressbar.after(delay, update)  # Schedule the next update
            if self.progress > 0.95:
                self.progressbar.set(1)

        update()
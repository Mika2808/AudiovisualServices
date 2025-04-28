import customtkinter
from change_container import ChangeContainerFrame
from change_resolution import ChangeResolutionFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # main parameters
        self.title("Name Surname")
        self.geometry("1000x800")
        customtkinter.set_widget_scaling(1.3)  # widget dimensions and text size
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.current_frame = None
        self.show_main_frame()

    def show_main_frame(self):
        self.show_frame(MainFrame)
        
    def show_frame(self, frame):
        # delete current scene
        if self.current_frame is not None:
            self.current_frame.destroy()

        # creating new scene
        self.current_frame = frame(self)
        self.current_frame.grid(row=0, column=0, sticky="nsew")
    
    def exit(self):
        #print("Exiting") # info
        self.destroy() # destroying object
    

        
class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.start_frame = customtkinter.CTkLabel(
            self,
            text="🎬 Welcome to the FFMPEG GUI",
            fg_color="#3a3a3a",
            text_color="white",
            corner_radius=12,
            font=("Arial", 24, "bold")
        )
        self.start_frame.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="nsew")

        self.options = {"Change container/codec" : ChangeContainerFrame, 
                        "Change resolution" : ChangeResolutionFrame, 
                        "Change CRF" : None, 
                        "Cut video" : None, 
                        "Extract audio" : None, 
                        "Merge videos" : None, 
                        "Exit" : None
                        }

        for i, option in enumerate(self.options):
            if option == "Exit":
                self.button = customtkinter.CTkButton(
                self,
                text=option,
                command=lambda option=option: self.choose_option(option),
                fg_color="transparent",
                hover_color="red",
                corner_radius=10,
                font=("Arial", 18)
                )
                self.button.grid(row=i+2, column=0, padx=20, pady=15, sticky="ew", columnspan=2)
            else:
                self.button = customtkinter.CTkButton(
                    self,
                    text=option,
                    command=lambda option=option: self.choose_option(option),
                    fg_color="transparent",
                    hover_color="#357ABD",
                    corner_radius=10,
                    font=("Arial", 18)
                )
                self.button.grid(row=i+2, column=0, padx=20, pady=15, sticky="ew", columnspan=2)
        
    def choose_option(self, option):
        #print("Button clicked:", option) # info about clicked button
        
        # changing frame or exiting
        if option == "Exit":
            self.master.exit()  
        else:
            self.master.show_frame(self.options[option])

app = App()
app.mainloop()




## Dictionary for resolution
# self.resolutions = {
#     "Original (no change)": "scale=iw:ih",
#     "Full HD (1920x1080)": "scale=1920:1080",
#     "HD (1280x720)": "scale=1280:720",
#     "SD (640x480)": "scale=640:480",
#     "480p (854x480)": "scale=854:480",
#     "360p (640x360)": "scale=640:360",
#     "240p (426x240)": "scale=426:240",
#     "Fit width 1280 (keep aspect)": "scale=1280:-1",
#     "Fit height 720 (keep aspect)": "scale=-1:720",
#     "Fit width 640 (keep aspect)": "scale=640:-1",
#     "Fit height 480 (keep aspect)": "scale=-1:480"
# }

## CRF
# self.resolutions = {
#     "Original (no change)": "scale=iw:ih",
#     "Full HD (1920x1080)": "scale=1920:1080",
#     "HD (1280x720)": "scale=1280:720",
#     "SD (640x480)": "scale=640:480",
#     "480p (854x480)": "scale=854:480",
#     "360p (640x360)": "scale=640:360",
#     "240p (426x240)": "scale=426:240",
#     "Fit width 1280 (keep aspect)": "scale=1280:-1",
#     "Fit height 720 (keep aspect)": "scale=-1:720",
#     "Fit width 640 (keep aspect)": "scale=640:-1",
#     "Fit height 480 (keep aspect)": "scale=-1:480"
# }

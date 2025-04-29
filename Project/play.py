import customtkinter
import subprocess
from tkinter import filedialog
import os

class PlayFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Play video",
            fg_color="#3a3a3a",
            text_color="white",
            corner_radius=12,
            font=("Arial", 24, "bold")
        )        
        self.title_frame.grid(row=0, column=0, columnspan=6, padx=10, pady=(20, 10), sticky="news")

        # Upload button 
        self.upload_file_button = customtkinter.CTkButton(
            self,
            text="Upload file",
            command=self.upload_file,
            fg_color="transparent",
            hover_color="#357ABD",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.upload_file_button.grid(row=2, column=0, columnspan=6, padx=20, pady=15, sticky="new")

        # Label for filepath to show what was chosen
        self.file_label = customtkinter.CTkLabel(
            self,
            text="No file selected",
            text_color="black",
            fg_color="white", 
            corner_radius= 10,
            font=("Arial", 14)
        )
        self.file_label.grid(row=3, column=0, columnspan=6, padx=20, pady=10, sticky="new")

        # Exit button
        self.exit_button = customtkinter.CTkButton(
            self,
            text="Go back",
            command=self.choose_option,
            fg_color="transparent",
            hover_color="red",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.exit_button.grid(row=8, column=0, padx=20, pady=15, sticky="w")
        
        # Do operation button
        self.do_the_thing_button = customtkinter.CTkButton(
            self,
            text="Do the thing!",
            command=self.do_the_thing,
            fg_color="transparent",
            hover_color="green",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.do_the_thing_button.grid(row=8, column=4, padx=20, pady=15, sticky="e")

    # def option_changed(self, selected_option):
    #     print(f"Selected: {selected_option}")

    def choose_option(self):
        #print("Go back to main frame")
        self.master.show_main_frame()
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")],
            initialdir="/home/mikab/Maribor/Studia/AUDIOVISUAL SERVICES/Project/Videos/Individual"
        )
        if file_path:
            self.file_label.configure(text=f"{file_path}")
            #print(f"File selected: {file_path}")
        else:
            self.file_label.configure(text="No file selected")
        
    def do_the_thing(self):
        if self.check_file() is True:

            cmd = [ "ffplay", "-i", self.file_label.cget("text")]
            subprocess.run(cmd, check=True)
                        
        else:
            print("Do the thing not done because of wrong extension of chosen file!")
    
    def check_file(self):
        # checking if file has good extension
        if self.file_label.cget("text") == "No file selected":
            return False
        else:
            filename, extension = os.path.splitext(self.file_label.cget("text"))
            if extension in [".mp4", ".mkv", ".avi", ".mov", ".webm", ".flv"]:
                return True
            else:
                return False

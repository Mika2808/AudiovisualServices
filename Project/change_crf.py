import customtkinter
import subprocess
from tkinter import filedialog
import os

class ChangeCRFFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Change CRF - Constant Rate Factor",
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

        # Label choosing resolution
        self.crf_label = customtkinter.CTkLabel(
            self,
            text="CRF:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.crf_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="e")

        # Dictonary for resolutions
        self.crfs = {
            "Default (23)": "23",
            "Very High Quality (18)": "18",
            "High Quality (20)": "20",
            "Good Quality (23)": "23",
            "Balanced (25)": "25",
            "Low Quality (28)": "28",
            "Very Low Quality (50)": "50"
        }


        # Resolution options
        self.crf_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=list(self.crfs.keys()),
            #command=self.option_changed  # callback when selected
        )
        self.crf_option_menu.grid(row=4, column=3, padx=20, pady=10, sticky="w")

        # Preview button 
        self.preview_button = customtkinter.CTkButton(
            self,
            text="Preview",
            command=self.preview,
            fg_color="transparent",
            hover_color="#357ABD",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.preview_button.grid(row=7, column=0, columnspan=6, padx=20, pady=15, sticky="new")

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
    
    def preview(self):
        if self.check_file() is True:       
            output_preview = "preview.mov"

            # creating short version
            cmd = [
                "ffmpeg",
                "-y",
                "-ss", "00:00:40",
                "-i", self.file_label.cget("text"),
                "-t", "3",
                "-crf", self.crfs[self.crf_option_menu.get()], # changing resoultion
                output_preview
            ]
            subprocess.run(cmd, check=True)
            
            # playing short version
            cmd = ["ffplay", output_preview]
            subprocess.run(cmd, check=True)

            # deleting short version
            if os.path.exists(output_preview):
                os.remove(output_preview)
            else:
                print(f"Preview file {output_preview} not found!")
                
        else:
            print("Preview not done because of wrong extension of chosen file!")

    
    def do_the_thing(self):
        directory_path = filedialog.askdirectory(
        title="Select a directory for new file",
        initialdir="/home/mikab/Maribor/Studia/AUDIOVISUAL SERVICES/Project/Videos"
        )
        if directory_path:
            #print(f"Directory selected: {directory_path}")

            if self.check_file() is True:       
                filename, extension = os.path.splitext(self.file_label.cget("text"))
                output_preview = directory_path + "/FFMPEG_Graphical_CRF" + extension

                # creating new file
                cmd = [
                    "ffmpeg",
                    "-y",
                    "-i", self.file_label.cget("text"),
                    "-crf", self.crfs[self.crf_option_menu.get()], # changing resolution
                    output_preview
                ]
                subprocess.run(cmd, check=True)
                         
            else:
                print("Preview not done because of wrong extension of chosen file!")
        else:
            print("Directory not selected")

    
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

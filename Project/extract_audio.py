import customtkinter
import subprocess
from tkinter import filedialog
import os

class ExtractAudioFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Extract audio",
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
        self.audio_container_label = customtkinter.CTkLabel(
            self,
            text="Audio container:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.audio_container_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="e")

        # Dictonary for audio containers
        self.audio_containers = {
            "MP3 (MPEG Layer III)": ".mp3",
            "AAC (Advanced Audio Coding)": ".aac",
            "WAV (Uncompressed)": ".wav",
            "OGG (Vorbis)": ".ogg",
            "FLAC (Lossless)": ".flac",
            "Opus (Web-friendly)": ".opus",
            "M4A (MPEG-4 Audio)": ".m4a",
        }

        # Audio containers options
        self.audio_container_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=list(self.audio_containers.keys()),
            #command=self.option_changed  # callback when selected
        )
        self.audio_container_option_menu.grid(row=4, column=3, padx=20, pady=10, sticky="w")

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
            output_preview = "preview" + self.audio_containers[self.audio_container_option_menu.get()]

            # creating short version
            cmd = [ "ffmpeg",
                    "-ss", "00:00:40",
                    "-t", "3",
                    "-i", self.file_label.cget("text"),
                    "-q:a", "0", # highest quality
                    "-map", "a", # map only aduio stream
                    output_preview]
            
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
                
                output_preview = "FFMPEG_Graphical_Extracted_Audio" + self.audio_containers[self.audio_container_option_menu.get()]

                cmd = [ "ffmpeg", 
                        "-i", self.file_label.cget("text"),
                        "-q:a", "0", # highest quality
                        "-map", "a", # map only aduio stream
                        output_preview]
                subprocess.run(cmd, check=True)
                         
            else:
                print("Do the thing not done because of wrong extension of chosen file!")
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

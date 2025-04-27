import customtkinter
import subprocess
from tkinter import filedialog
import os

class ChangeContainerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Change container/codec",
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

        # Label choosing container
        self.container_label = customtkinter.CTkLabel(
            self,
            text="Container:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.container_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="e")

        # Dictonary for containers
        self.containers = {
            "MP4 (Most popular, Streaming)": ".mp4",
            "MKV (Flexible, Supports Everything)": ".mkv",
            "AVI (Old, Big Files)": ".avi",
            "MOV (Apple / QuickTime format)": ".mov",
            "WebM (Web Optimized, Open Source)": ".webm",
            "FLV (Flash Video, Older Web Videos)": ".flv"
        }

        # Container options
        self.container_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=list(self.containers.keys()),
            command=self.option_changed  # callback when selected
        )
        self.container_option_menu.grid(row=4, column=3, padx=20, pady=10, sticky="w")

        # Label choosing video codec
        self.video_codec_label = customtkinter.CTkLabel(
            self,
            text="Video codec:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.video_codec_label.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="e")

        # Dictionary with video codecs with values for FFMPEG        
        self.video_codecs = {
            "H.264 (High Quality / Compatibility)": "libx264",
            "H.265 (Better Compression, 4K Ready)": "libx265",
            "VP9 (Open Source, Web Optimized)": "libvpx-vp9",
            "AV1 (Future Format, Ultra Compression)": "libaom-av1",
            "MPEG-4 Part 2 (Old AVI videos)": "mpeg4"
        }

        # Video codec options
        self.video_codec_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=list(self.video_codecs.keys()),
            command=self.option_changed  # callback when selected
        )
        self.video_codec_option_menu.grid(row=5, column=3,columnspan=3, padx=20, pady=10, sticky="w")

        # Label choosing audio codec
        self.audio_codec_label = customtkinter.CTkLabel(
            self,
            text="Audio codec:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.audio_codec_label.grid(row=6, column=0,columnspan=3, padx=20, pady=10, sticky="e")

        # Dictionary with audio codecs with values for FFMPEG   
        self.audio_codecs = {
            "AAC (Best for MP4 / Streaming)": "aac",
            "MP3 (Classic, Wide Support)": "libmp3lame",
            "Opus (Modern, Low Latency)": "libopus",
            "FLAC (Lossless, Best Quality)": "flac",
            "AC3 (Dolby Surround Sound)": "ac3"
        }

        # Audio codec options
        self.audio_codec_option_menu = customtkinter.CTkOptionMenu(
            self,
            values=list(self.audio_codecs.keys()),
            command=self.option_changed  # callback when selected
        )
        self.audio_codec_option_menu.grid(row=6, column=3, columnspan=3, padx=20, pady=10, sticky="w")

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

    def option_changed(self, selected_option):
        print(f"Selected: {selected_option}")


    def choose_option(self):
        print("Go back to main frame")
        self.master.show_main_frame()
    
    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Select a File",
            filetypes=[("All Files", "*.*")],
            initialdir="/home/mikab/Maribor/Studia/AUDIOVISUAL SERVICES/Project/Videos/Individual"
        )
        if file_path:
            self.file_label.configure(text=f"{file_path}")
            print(f"File selected: {file_path}")
        else:
            self.file_label.configure(text="No file selected")
    
    def preview(self):
        if self.check_file() is True:
            output_preview = "output.mov"

            # creating short version
            cmd = [
                "ffmpeg",
                "-y",
                "-ss", "00:00:40",
                "-i", self.file_label.cget("text"),
                "-t", "3",
                "-c", "copy",
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
        print("lets go")
    
    def check_file(self):
        if self.file_label.cget("text") == "No file selected":
            return False
        else:
            filename, extension = os.path.splitext(self.file_label.cget("text"))
            if extension in self.containers.values():
                return True
            else:
                return False
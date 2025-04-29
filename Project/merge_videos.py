import customtkinter
from tkinter import filedialog
import subprocess
import os

class MergeVideosFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Merge videos",
            fg_color="#3a3a3a",
            text_color="white",
            corner_radius=12,
            font=("Arial", 24, "bold")
        )        
        self.title_frame.grid(row=0, column=0, columnspan=6, padx=10, pady=(20, 10), sticky="news")

        self.select_button = customtkinter.CTkButton(self, text="Select Videos", command=self.select_videos)
        self.select_button.grid(row=2, column=0, columnspan=6, padx=20, pady=15, sticky="new")


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

        self.selected_files = []

    def select_videos(self):
        selected_file = filedialog.askopenfilename(
            title="Select video files to merge",
            filetypes=[("Video files", "*.mp4 *.mov *.mkv *.ts *.avi")]
        )
        if selected_file:
            self.selected_files.append(selected_file)
            print("Selected files:")
            for f in self.selected_files:
                print(f)

    def do_the_thing(self):
        if not self.selected_files:
            print("No files selected.")
            return

        # Create temporary file list
        file_list_path = "file_list.txt"
        with open(file_list_path, "w") as f:
            for path in self.selected_files:
                f.write(f"file '{path}'\n")

        directory_path = filedialog.askdirectory(
        title="Select a directory for new file",
        initialdir="/home/mikab/Maribor/Studia/AUDIOVISUAL SERVICES/Project/Videos"
        )

        output_file = directory_path + "/FFMPEG_Graphical_Merged.mp4"
        cmd = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", file_list_path,
            "-c", "copy",
            output_file
        ]
        subprocess.run(cmd, check=True)

        # deleting short version
        if os.path.exists(file_list_path):
            os.remove(file_list_path)
        else:
            print(f"Preview file {file_list_path} not found!")

        print(f"Merged file created: {output_file}")
    
    def choose_option(self):
        #print("Go back to main frame")
        self.master.show_main_frame()
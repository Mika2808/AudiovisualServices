import customtkinter
from tkinter import filedialog
import subprocess
import os

class MergeVideosFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.select_button = customtkinter.CTkButton(self, text="Select Videos", command=self.select_videos)
        self.select_button.pack(pady=10)

        self.merge_button = customtkinter.CTkButton(self, text="Merge Videos", command=self.merge_videos)
        self.merge_button.pack(pady=10)

        self.selected_files = []

    def select_videos(self):
        selected_file = filedialog.askopenfilenames(
            title="Select video files to merge",
            filetypes=[("Video files", "*.mp4 *.mov *.mkv *.ts *.avi")]
        )
        if selected_file:
            self.selected_files.append(selected_file)
            print("Selected files:")
            for f in self.selected_files:
                print(f)

    def merge_videos(self):
        if not self.selected_files:
            print("No files selected.")
            return

        # Create temporary file list
        file_list_path = "file_list.txt"
        with open(file_list_path, "w") as f:
            for path in self.selected_files:
                f.write(f"file '{path}'\n")

        # Run FFmpeg command
        output_file = "merged_output.mp4"
        cmd = [
            "ffmpeg",
            "-f", "concat",
            "-safe", "0",
            "-i", file_list_path,
            "-c", "copy",
            output_file
        ]
        print("Running:", " ".join(cmd))
        subprocess.run(cmd, check=True)

        print(f"Merged file created: {output_file}")
import customtkinter
import subprocess
from tkinter import filedialog
import os

class CutVideoFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,2,3), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Title
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Cut video",
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

        # Label for starting point of cutting
        self.starting_point_label = customtkinter.CTkLabel(
            self,
            text="Starting point:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.starting_point_label.grid(row=4, column=0, columnspan=3, padx=20, pady=10, sticky="e")
        
        # Starting point Entry
        self.starting_point_entry = customtkinter.CTkEntry(master=self, corner_radius=0, placeholder_text="00:00:00")
        self.starting_point_entry.grid(row=4, column=3, padx=20, pady=10, sticky="w")

        # Label ending point of cutting
        self.ending_point_label = customtkinter.CTkLabel(
            self,
            text="Ending point:",
            text_color="white",
            fg_color="transparent",
            font=("Arial", 18)
        )
        self.ending_point_label.grid(row=5, column=0, columnspan=3, padx=20, pady=10, sticky="e")
        
        # Ending point Entry
        self.ending_point_entry = customtkinter.CTkEntry(master=self, corner_radius=0, placeholder_text="00:00:00")
        self.ending_point_entry.grid(row=5, column=3,columnspan=3, padx=20, pady=10, sticky="w")

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
                "-t", str(self.count_time(self.starting_point_entry.get(), self.ending_point_entry.get())), 
                output_preview
            ]
            subprocess.run(cmd, check=True)
            
            # playing short version
            cmd = ["ffplay", output_preview]
            subprocess.run(cmd, check=True)

            # # deleting short version
            # if os.path.exists(output_preview):
            #     os.remove(output_preview)
            # else:
            #     print(f"Preview file {output_preview} not found!")
                
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
                output_preview = "FFMPEG_Graphical_Cut_Video" + extension

                # creating new file
                cmd = [
                    "ffmpeg",
                    "-y",
                    "-ss", "00:00:40",
                    "-i", self.file_label.cget("text"),
                    "-t", str(self.count_time(self.starting_point_entry.get(), self.ending_point_entry.get())),
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
    
    def count_time(self, starting_point, ending_point):

        seconds_string = int(ending_point[6:8]) - int(starting_point[6:8])
        minutes_string = int(ending_point[3:5]) - int(starting_point[3:5])
        hours_string = int(ending_point[0:2]) - int(starting_point[0:2])

        return seconds_string + minutes_string*60 + hours_string*60*60

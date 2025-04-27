import customtkinter
import subprocess

class ChangeContainerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.title_frame = customtkinter.CTkLabel(
            self,
            text="Change container/codec",
            fg_color="#3a3a3a",
            text_color="white",
            corner_radius=12,
            font=("Arial", 24, "bold")
        )
        
        self.title_frame.grid(row=0, column=0, columnspan=6, rowspan=2, padx=10, pady=(20, 10), sticky="new")

        self.exit_button = customtkinter.CTkButton(
            self,
            text="Go back",
            command=self.choose_option,
            fg_color="transparent",
            hover_color="#357ABD",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.exit_button.grid(row=6, column=0, padx=20, pady=15, sticky="w")
        
    def choose_option(self):
        print("Go back to main frame")
        self.master.show_main_frame()
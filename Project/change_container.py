import customtkinter
import subprocess

class ChangeContainerFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="#2b2b2b", **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.start_frame = customtkinter.CTkLabel(
            self,
            text="Change container!!!!!!!!!!!!!!!",
            fg_color="#3a3a3a",
            text_color="white",
            corner_radius=12,
            font=("Arial", 24, "bold")
        )
        self.start_frame.grid(row=0, column=0, padx=10, pady=(20, 10), sticky="nsew")

        self.button = customtkinter.CTkButton(
            self,
            text="Tralalala",
            command=self.choose_option,
            fg_color="transparent",
            hover_color="#357ABD",
            corner_radius=10,
            font=("Arial", 18)
        )
        self.button.grid(row=2, column=0, padx=20, pady=15, sticky="ew", columnspan=2)
        
    def choose_option(self):
        print("Button was clicked, button was clicked!")
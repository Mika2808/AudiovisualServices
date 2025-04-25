import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Mikołaj Kabała")
        self.geometry("800x500")
        customtkinter.set_widget_scaling(1.3)  # widget dimensions and text size
        #self.starting_frame = StartingFrame(self)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        self.start_frame = customtkinter.CTkLabel(self, text="Welcome to graphical interface for FFMPEG", fg_color="gray30", corner_radius=10)
        self.start_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
    def button_callback(self):
        print("Button")
        
        

    
class StartingFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        
        self.start_frame = customtkinter.CTkLabel(self, text="Welcome to graphical interface for FFMPEG", fg_color="gray30", corner_radius=10)
        self.start_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
    def button_callback(self):
        print("Button")


app = App()
app.mainloop()
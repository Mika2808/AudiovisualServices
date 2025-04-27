import customtkinter

from typing import Union
from typing import Callable

class WidgetName(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

class FloatSpinbox(customtkinter.CTkFrame):
    def __init__(self, *args,
                 width: int = 100,
                 height: int = 32,
                 step_size: Union[int, float] = 1,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.step_size = step_size
        self.command = command

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.grid_columnconfigure((0, 2), weight=0)  # buttons don't expand
        self.grid_columnconfigure(1, weight=1)  # entry expands

        self.subtract_button = customtkinter.CTkButton(self, text="-", width=height-6, height=height-6,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=width-(2*height), height=height-6, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, text="+", width=height-6, height=height-6,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)

        # default value
        self.entry.insert(0, "0.0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = float(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self) -> Union[float, None]:
        try:
            return float(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(float(value)))

class MyCheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyRadiobuttonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i + 1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()

    def set(self, value):
        self.variable.set(value)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        #self.checkbox_frame = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])
        #self.checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        #self.radiobutton_frame = MyRadiobuttonFrame(self, "Options", values=["option 1", "option 2"])
        #self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nesw")
        #self.radiobutton_frame.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        
    def button_callback(self):
        print("checkbox_frame", self.scrollable_checkbox_frame.get())
        #print("radiobutton_frame", self.radiobutton_frame.get(), "\n")


class ExampleApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Option Menu Example")
        self.geometry("400x200")

        self.option_menu = customtkinter.CTkOptionMenu(
            self,
            values=["Option 1", "Option 2", "Option 3"],
            command=self.option_changed  # callback when selected
        )
        self.option_menu.pack(pady=20)

        self.label = customtkinter.CTkLabel(self, text="Choose something...")
        self.label.pack(pady=10)

    def option_changed(self, selected_option):
        print(f"Selected: {selected_option}")
        self.label.configure(text=f"You chose: {selected_option}")

app = App()
app.mainloop()

## ADVANCED
# app = customtkinter.CTk()

# spinbox_1 = FloatSpinbox(app, width=150, step_size=3)
# spinbox_1.pack(padx=20, pady=20)

# spinbox_1.set(35)
# print(spinbox_1.get())

# app.mainloop()
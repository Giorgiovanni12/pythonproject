import tkinter as tk
from tkinter import ttk, PhotoImage
import speech_recognition as sr


class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter GUI")
        self.geometry("300x300")

        # Load an image for the background
        self.background_image = PhotoImage(file="/home/giorgio/papa-massimo/MIao/ErChicoria.png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a style object to control the appearance of the widgets
        self.style = ttk.Style(self)
        self.style.theme_use('default')

        # Define the color schemes for the light and dark themes
        self.light_theme = {"bg": "white", "fg": "black"}
        self.dark_theme = {"bg": "black", "fg": "white"}

        # Create two buttons
        self.button1 = ttk.Button(self, text="Trascrivi il file selezionato da wav a txt")
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self, text="Riassumi il file selezionato")
        self.button2.pack(pady=10)

        # Create a check button to switch between light and dark themes
        self.theme_var = tk.BooleanVar()
        self.theme_checkbutton = ttk.Checkbutton(self, text="Dark theme", variable=self.theme_var, command=self.switch_theme)
        self.theme_checkbutton.pack(pady=10)

    def switch_theme(self):
        if self.theme_var.get():
            self.style.configure("TButton", foreground=self.dark_theme["fg"], background=self.dark_theme["bg"])
            self.configure(background=self.dark_theme["bg"])
        else:
            self.style.configure("TButton", foreground=self.light_theme["fg"], background=self.light_theme["bg"])
            self.configure(background=self.light_theme["bg"])

if __name__ == "__main__":
    app = Application()
    app.mainloop()

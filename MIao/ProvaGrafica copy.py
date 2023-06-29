import tkinter as tk
from tkinter import ttk, PhotoImage, filedialog
import speech_recognition as sr

def transcribe_audio_file(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Non si riesce a comprendere il contenuto del file")
    except sr.RequestError as e:
        print(f"Speech Recognition di google non funziona :( {e}")

def split_text_into_lines(text, max_words_per_line):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        current_line.append(word)
        if len(current_line) == max_words_per_line:
            lines.append(" ".join(current_line))
            current_line = []

    if current_line:
        lines.append(" ".join(current_line))

    return lines

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
        self.button1 = ttk.Button(self, text="Trascrivi il file selezionato da wav a txt", command=self.transcribe)
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

    def transcribe(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file_path:
            transcribed_text = transcribe_audio_file(file_path)
            if transcribed_text:
                print("Trascrizione per intera del testo:")
                print(transcribed_text)
                formatted_text = split_text_into_lines(transcribed_text, 15)
                with open("tradotto.txt", "w") as output_file:
                    for line in formatted_text:
                        output_file.write(line + "\n")
            else:
                print("Impossibile trascrivere :(")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

import tkinter as tk
from tkinter import ttk, PhotoImage, filedialog
import speech_recognition as sr
import openai
import re
from PIL import Image
from screeninfo import get_monitors

openai.api_key = "add your api key"  # OpenAI Key

def get_screen_resolution():  # Get screen resolution function
    monitor = get_monitors()[0]
    return monitor.width, monitor.height

def resize_image(image_path):  # Resize image function
    img = Image.open(image_path)
    screen_width, screen_height = get_screen_resolution()
    img = img.resize((screen_width, screen_height), Image.ADAPTIVE)
    img.save("Main_PY/building_with_python_watermark (1).png")

resize_image("Main_PY/building_with_python_watermark (1).png")

def transcribe_audio_file(audio_file_path):  # Function to transcribe the file handling potential errors
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Unable to comprehend the content of the file")
    except sr.RequestError as e:
        print(f"Google Speech Recognition is not working :( {e}")

def summarize_text(text):  # OpenAI prompt function to summarize the given text, ignoring any links
    text = re.sub(r'http\S+', '', text)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n{text}\n\nSummary:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    summary = response.choices[0].text.strip()

    return summary

def split_text_into_lines(text, max_words_per_line):  # Function to split words and line break consistently
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

        self.title("Notepad +++")
        self.geometry("300x300")

        # Load an image in the background
        self.background_image = PhotoImage(file="Main_PY/building_with_python_watermark (1).png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create GUI style
        self.style = ttk.Style(self)
        self.style.theme_use('default')

        # Define parameters for light and dark themes
        self.light_theme = {"bg": "white", "fg": "black"}
        self.dark_theme = {"bg": "black", "fg": "white"}

        # Create buttons for two actions Transcribe/Summarize
        self.button1 = ttk.Button(self, text="Transcribe the selected wav file to txt", command=self.transcribe)
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self, text="Summarize the selected file", command=self.summarize)
        self.button2.pack(pady=10)

        # Switch for light/dark theme
        self.theme_var = tk.BooleanVar()
        self.theme_checkbutton = ttk.Checkbutton(self, text="Light/Dark Theme", variable=self.theme_var, command=self.switch_theme)
        self.theme_checkbutton.pack(pady=10)
        
        # Create a button that provides some information about the project
        self.button = ttk.Button(self, text="Information", command=self.open_dialog)
        self.button.pack(pady=20)

    def open_dialog(self):  # Function to open the popup with information
        dialog = tk.Toplevel(self)

        text_label = ttk.Label(dialog, text="\nThe program is designed to take a wav file and transform it into a text file.\nThe second button aims to summarize the content of the text file.\nFor any additional information")
        text_label.pack(pady=20)

        close_button = ttk.Button(dialog, text="Close", command=dialog.destroy)
        close_button.pack(pady=20)

    def switch_theme(self):  # Function to change button themes
        if self.theme_var.get():
            self.style.configure("TButton", foreground=self.dark_theme["fg"], background=self.dark_theme["bg"])
            self.configure(background=self.dark_theme["bg"])
        else:
            self.style.configure("TButton", foreground=self.light_theme["fg"], background=self.light_theme["bg"])
            self.configure(background=self.light_theme["bg"])

    def transcribe(self):  # Function that uses transcribe_audio_file
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav")])
        if file_path:
            transcribed_text = transcribe_audio_file(file_path)
            if transcribed_text:
                print("Transcription of the entire text:")
                print(transcribed_text)
                formatted_text = split_text_into_lines(transcribed_text, 15)
                with open("translated.txt", "w") as output_file:
                    for line in formatted_text:
                        output_file.write(line + "\n")
            else:
                print("Unable to transcribe :(")

    def summarize(self):  # Function that uses summarize_text
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as input_file:
                text = input_file.read()

            summary = summarize_text(text)

            print("Original Text:")
            print(text)
            print("\nSummary:")
            print(summary)

            summary = split_text_into_lines(summary, 15)

            with open("summary.txt", "w") as output_file:
                for line in summary:
                    output_file.write(line + "\n")
                print("Transcription successful :)")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

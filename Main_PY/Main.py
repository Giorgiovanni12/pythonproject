import tkinter as tk
from tkinter import ttk, PhotoImage, filedialog
import speech_recognition as sr
import openai
import re
from PIL import Image
from screeninfo import get_monitors

openai.api_key = "add your api key"  #Chiave di OpenAI 



def get_screen_resolution(): #Per avere la risoluzione dello schermo
    monitor = get_monitors()[0]
    return monitor.width, monitor.height

def resize_image(image_path): #Per ritagliare l'immagine
    img = Image.open(image_path)
    screen_width, screen_height = get_screen_resolution()
    img = img.resize((screen_width, screen_height), Image.ADAPTIVE)
    img.save("Main_PY/building_with_python_watermark (1).png")

resize_image("Main_PY/building_with_python_watermark (1).png")


def transcribe_audio_file(audio_file_path): #funzione per trascrivere il file gestendo anche gli eventuali errori
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

def summarize_text(text): ##Prompt di OpenAi con lo scopo di riassumere il seguente testo,non prendendo in considerazione eventuali link
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

def split_text_into_lines(text, max_words_per_line): #funzione per dividere le parole e andare a capo con costanza
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

        # Serve per caricare un immagine in background
        self.background_image = PhotoImage(file="Main_PY/building_with_python_watermark (1).png")
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #  Serve per creare lo stile della GUI
        self.style = ttk.Style(self)
        self.style.theme_use('default')

        #  Serve per definire i parametri dei temi scuri e chiari
        self.light_theme = {"bg": "white", "fg": "black"}
        self.dark_theme = {"bg": "black", "fg": "white"}

        # Creare i bottoni per le due azioni Trascrivere/Riassumere
        self.button1 = ttk.Button(self, text="Trascrivi il file selezionato da wav a txt", command=self.transcribe)
        self.button1.pack(pady=10)

        self.button2 = ttk.Button(self, text="Riassumi il file selezionato", command=self.summarize)
        self.button2.pack(pady=10)

        # Swith per lo stile chiaro/scuro
        self.theme_var = tk.BooleanVar()
        self.theme_checkbutton = ttk.Checkbutton(self, text="Tema Chiaro/Scuro", variable=self.theme_var, command=self.switch_theme)
        self.theme_checkbutton.pack(pady=10)
        #Creare un bottone che dia alcune indicazioni per il progetto
        self.button = ttk.Button(self, text="Informazioni", command=self.open_dialog)
        self.button.pack(pady=20)

    def open_dialog(self):  #funzione per aprire il popup con le informazioni
        dialog = tk.Toplevel(self)

        text_label = ttk.Label(dialog, text="\nIl programma ha lo scopo di prendere un file in formato wav e di trasformarlo in file di testo.\nIl secondo bottone ha lo scopo di riassumere il contenuto del file di testo.\nPer qualsiasi informazione aggiuntiva scrivere alla mail giovanni.sello@edu.itspiemonte.it")
        text_label.pack(pady=20)

        close_button = ttk.Button(dialog, text="Chiudi", command=dialog.destroy)
        close_button.pack(pady=20)

        

    def switch_theme(self): #funzione per cambiare il tema dei bottoni
        if self.theme_var.get():
            self.style.configure("TButton", foreground=self.dark_theme["fg"], background=self.dark_theme["bg"])
            self.configure(background=self.dark_theme["bg"])
        else:
            self.style.configure("TButton", foreground=self.light_theme["fg"], background=self.light_theme["bg"])
            self.configure(background=self.light_theme["bg"])

    def transcribe(self): #funzione che riprende transcribe_audio_file 
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

    def summarize(self): #funzione che riprende summarize_text
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "r") as input_file:
                text = input_file.read()

            summary = summarize_text(text)

            print("Testo originale:")
            print(text)
            print("\nSommario:")
            print(summary)

            summary = split_text_into_lines(summary, 15)

            with open("riassunto.txt", "w") as output_file:
                for line in summary:
                    output_file.write(line + "\n")
                print("Trascrizione riuscita :)")

if __name__ == "__main__":
    app = Application()
    app.mainloop()

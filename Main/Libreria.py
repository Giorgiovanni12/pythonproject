import tkinter as tk
from tkinter import ttk, PhotoImage, filedialog
import speech_recognition as sr
import openai
import re


def transcribe_audio_file(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)
                                                                #funzione per trascrivere il file 
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


def summarize_text(text):
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


def summarize(self):
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
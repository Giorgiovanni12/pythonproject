import tkinter as tk
from tkinter import ttk, filedialog
import speech_recognition as sr
class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("My GUI")
        
        # Create a main frame
        self.main_frame = ttk.Frame(master, padding="10")
        self.main_frame.pack()

        # Create a label
        self.label = ttk.Label(self.main_frame, text="Puoi trasformare i tuoi file audio in file di testo!")
        self.label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Create a button to open a file
        self.open_button = ttk.Button(self.main_frame, text="Seleziona il file", command=self.open_file)
        self.open_button.grid(row=1, column=0, pady=(0, 10))

        # Create a button to save the new file
        self.save_button = ttk.Button(self.main_frame, text="Scarica il file nel tuo calcolatore", command=self.save_file)
        self.save_button.grid(row=1, column=1, pady=(0, 10))



        # Load the background image
        self.background_image = tk.PhotoImage(file="download.png")

        # Create a canvas to display the background image
        self.canvas = tk.Canvas(master, width=self.background_image.width(), height=self.background_image.height())
        self.canvas.pack()

        # Display the background image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)

        # Create a main frame
        self.main_frame = ttk.Frame(master, padding="10")
        self.main_frame.place(x=10, y=10)  # Adjust the position of the main frame

        # Add the rest of your widgets to the main_frame as before
        # ...
      
        self.open_button=ttk.Button(self.main_frame, text="Apri una nuova Pagina <3>", command=self.open_new_window)
        self.open_button.grid(row=43, column=21, pady=(0, 10))

        self.file_path = None

    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            with open(self.file_path, 'r') as file:
                content = file.read()
                self.textbox.delete(1.0, tk.END)
                self.textbox.insert(tk.END, content)

    def save_file(self):
        if self.file_path:
            new_file_path = filedialog.asksaveasfilename()
            if new_file_path:
                with open(new_file_path, 'w') as file:
                    content = self.textbox.get(1.0, tk.END)
                    processed_content = self.process_content(content)
                    file.write(processed_content)


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
            print(f"Speech Recognition di google non funge :( {e}")


    def split_text_into_lines(text, max_words_per_line):     #Serve per splittare le linee con la stessa lunhezza in termini di parole
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
    def process_content(self, content):
        # Implement your function here
        return content

    def open_new_window(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Nuova Finestra")
        new_window.geometry("300x200")
        ttk.Label(new_window, text="Miao").pack(pady=20)

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()

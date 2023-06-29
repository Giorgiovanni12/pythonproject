import speech_recognition as sr



input=input("Inserisci il path del file in formato wav:")
print("Inizia il Processo ")
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

if __name__ == "__main__":
    input = "/home/giorgio/papa-massimo/Notepad+++/How-To-Stop-Mumbling-Use-This-Quick-Technique.wav"  #Inserire il file in formato wav
    transcribed_text = transcribe_audio_file(input)

    if transcribed_text:
        print("Trascrizione per intero del testo:")
        print(transcribed_text)
        formatted_text = split_text_into_lines(transcribed_text, 15)
        with open("tradotto.txt", "w") as output_file:
            for line in formatted_text:
                output_file.write(line + "\n")
    else:
        print("Impossibile trascrivere :(")

print("Finito!")
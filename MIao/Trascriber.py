import speech_recognition as sr

print("Inizia il Processo ")
def transcribe_audio_file(audio_file_path):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

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

if __name__ == "__main__":
    audio_file_path = "MIao/X2Download.app-Online-Speech-Reception-Threshold-_SRT_-Hearing-Test-_128-kbps_.wav"
    transcribed_text = transcribe_audio_file(audio_file_path)

    if transcribed_text:
        print("Trascrizione per intera del testo:")
        print(transcribed_text)
        formatted_text = split_text_into_lines(transcribed_text, 1)
        with open("output.txt", "w") as output_file:
            for line in formatted_text:
                output_file.write(line + "\n")
    else:
        print("Impossibile trascrivere :(")

print("Finito!")
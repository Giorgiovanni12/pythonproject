import speech_recognition as sr
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

if __name__ == "__main__":
    audio_file_path = "MIao/X2Download.app-Online-Speech-Reception-Threshold-_SRT_-Hearing-Test-_128-kbps_.wav"
    transcribed_text = transcribe_audio_file(audio_file_path)

    if transcribed_text:
        print("Transcribed <3")
        words = transcribed_text.split()
        output_text = ""
        for i in range(0, len(words), 15):
            output_text += " ".join(words[i:i+15]) + "\n"
        with open("output.txt", "w") as output_file:
            output_file.write(output_text)
    else:
        print("No transcription available")

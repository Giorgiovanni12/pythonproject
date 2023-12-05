# Python Speech-to-Text and Summarization Script Guide

## Prerequisites

Before using the script, make sure you have the required Python libraries installed. You can install them using the following:
```bash

pip install tkinter pillow SpeechRecognition openai pyaudio
```

Additionally, you'll need to sign up for an OpenAI API key and replace the placeholder in the script with your key.

Script Overview

The provided Python script combines speech recognition using the SpeechRecognition library and text summarization using the OpenAI GPT-3 model.

Usage Steps

1. Install Required Libraries:
```bash
   pip install tkinter pillow SpeechRecognition openai pyaudio
```

3. Sign Up for OpenAI API Key:
   Visit OpenAI to sign up for an API key and replace the placeholder in the script with your key.

4. Run the Script:
 ```bash
  python main.py
  ```

6. GUI Interface:
   - The GUI will open with two main buttons: "Transcribe the selected wav file to txt" and "Summarize the selected file."
   - The "Light/Dark Theme" checkbox allows you to switch between light and dark themes.
   - The "Information" button provides details about the project.

7. Transcribing an Audio File:
   - Click the "Transcribe" button.
   - Select a WAV file when prompted.
   - The transcribed text will be printed in the console, and a formatted version will be saved in "translated.txt."

8. Summarizing a Text File:
   - Click the "Summarize" button.
   - Select a text file when prompted.
   - The original text, summary, and a formatted version of the summary will be printed in the console. The summary will also be saved in "summary.txt."

9. Additional Information:
   - The "Information" button opens a popup with information about the project, including contact details for further inquiries.

Troubleshooting

- If you encounter issues with speech recognition, ensure your microphone is working correctly and accessible.
- Verify that the provided OpenAI API key is correct and has the necessary permissions.

Notes

- Customize the script according to your project requirements.
- Feel free to contribute or enhance the functionality of the script.

Happy scripting!

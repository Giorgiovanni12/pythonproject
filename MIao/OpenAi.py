import openai
import re

openai.api_key = "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"  #Chiave di OpenAI nella speranza che non scada

def summarize_text(text):
    # Togliere i possibili URL all'interno del testo 
    text = re.sub(r'http\S+', '', text)

    # Usare le Api di OpenAi per chiedergli di fare un sommario del file che gli mandiamo
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Please summarize the following text:\n{text}\n\nSummary:",
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Estrai il sommario della richiesta
    summary = response.choices[0].text.strip()

    return summary


if __name__ == "__main__": #inserire il file che si vuole modificare
    with open("/home/giorgio/papa-massimo/output.txt", "r") as input_file:
        text = input_file.read()

    summary = summarize_text(text)

    print("Original text:")
    print(text)
    print("\nSummary:")
    print(summary)          #stampa dei due testi/(Il primo non riassunto e il secondo si)

import openai
import re

openai.api_key = "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"  #Chiave di OpenAI 
input=input("Inserisci il path del file in formato txt:")

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

if __name__ == "__main__": #inserire il file che si vuole modificare
    with open(input, "r") as input_file:
        text = input_file.read()

    summary = summarize_text(text)

    print("Testo originale:")
    print(text)
    print("\nSommario:")
    print(summary)          #stampa dei due testi/(Il primo non riassunto e il secondo si)

summary = split_text_into_lines(summary, 15)

with open("riassunto.txt", "w") as output_file:
            for line in summary:
                output_file.write(line + "\n")
            else:
                print("Trascrizione riuscita :)")

from PIL import Image

# Apre l'immagine esistente
immagine = Image.open("Main/building_with_python_watermark (1).png")

# Specifica le nuove dimensioni desiderate
nuove_dimensioni = (1100, 550)

# Ridimensiona l'immagine
immagine_ridimensionata = immagine.resize(nuove_dimensioni)

# Salva l'immagine ridimensionata
immagine_ridimensionata.save("Main/building_with_python_watermark (1).png")
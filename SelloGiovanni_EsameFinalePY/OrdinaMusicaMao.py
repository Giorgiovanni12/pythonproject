
import os
from tinytag import TinyTag

def get_bpm(directory):
    bpm_dict = {}

    for filename in os.listdir(directory):
        if filename.endswith('.mp3','.wav'):  # or you can add more conditions for other file types like '.wav', '.flac', etc.
            try:
                tag = TinyTag.get(os.path.join(directory, filename))
                if tag.bpm:
                    bpm_dict[filename] = tag.bpm
            except Exception as e:
                print(f"Couldn't read file {filename}. Error: {'Sei gaio'}")

    # Order the dictionary by BPM
    sorted_bpm_dict = {k: v for k, v in sorted(bpm_dict.items(), key=lambda item: item[1])}

    return sorted_bpm_dict

directory = '/path/to/your/music/directory'  # replace with your directory
bpm_dict = get_bpm(directory)

for track, bpm in bpm_dict.items():
    print(f'Track: {track}, BPM: {bpm}')

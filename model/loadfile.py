from tkinter import filedialog
import os
from pydub import AudioSegment 


def convert_to_wav(file):
    # Import audio file
    try:
        audio = AudioSegment.from_file(file.name)

    except:
        os.error('Something has gone horribly wrong (maybe not an audio file?)')
  
    # Create new filename
    new_filename = file.name.split('.')[0] + '.wav'
  
    # Export file as .wav
    audio.export(new_filename, format='wav')
     
    file.close()
    new_file = open(new_filename, 'r')

    return new_file


def prompt_audio_file():
    try:
        input = filedialog.askopenfile(mode='r')
    
    except FileNotFoundError:
        os.error('Incorrect File Given')
    
    filename = input.name
    is_wav = filename.endswith('.wav')

    if not is_wav:
        input = convert_to_wav(input)
    
    return input


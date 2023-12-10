import os
from scipy.io import wavfile
import numpy as np
from pydub import AudioSegment


class Model:
    def __init__(self):
        self.data = np.array()
        self.samplerate = 0

    """
    Gets data from an open file
    :param file:
    :return tuple(int, np.array)
    """
    def get_data(self, file):
        if not file.name.endswith('.wav'):
            print(f'clean_wav: {file.name} is not a wav file')
            return (0, [])
    
        samplerate, data = wavfile.read(file.name)
        return samplerate, np.array(data[:, 0])
    
    ##
    #   Updates model with input of new file
    #
    def update(self, file):
        samplerate, data = self.get_data(file)
        self.samplerate = samplerate
        self.data = data
    
    ##
    #   Exports a new wav file given a new audio file
    #
    def convert_to_wav(self, file):
        # Import audio file

        try:
            audio = AudioSegment.from_file(file.name)

        except:
            os.error('Something has gone horribly wrong (maybe not an audio file?)')
            print('Something has gone horribly wrong (maybe not an audio file?)')
            return None
      
        # Create new filename
        new_filename = file.name.split('.')[0] + '.wav'
      
        # Export file as .wav
        audio.export(new_filename, format='wav')
         
        file.close()
        new_file = open(new_filename, 'r')

        return new_file    


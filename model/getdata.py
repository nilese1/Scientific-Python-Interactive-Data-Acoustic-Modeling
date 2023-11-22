import os
from scipy.io import wavfile
import scipy.io

os.path.basename('../model')

import loadfile


"""Gets the data from an open file returns a tuple (samplerate, array(data))"""
def get_data(file):
    if not file.name.endswith('.wav'):
        print(f'clean_wav: {file.name} is not a wav file')
        return (0, [])
    
    samplerate, data = wavfile.read(file.name)
    return samplerate, data[:, 0]


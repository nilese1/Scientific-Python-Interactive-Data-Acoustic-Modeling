import os
from scipy.io import wavfile
from scipy.signal import welch
import numpy as np
from pydub import AudioSegment
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self.data = np.array([])
        self.samplerate = 0
        self.spectrum = [[]]
        self.freqs = []  # using low = 125, mid = 1k, high = 7.5k HZ
        self.t = [] # The times corresponding to midpoints of segments (i.e., the columns in spectrum)
        self.im = None # This won't be useful in the model 
        
        self.rt60_freqs = [200, 1000, 7500] # frequencies that will be searched through to find average
        self.rt60 = 0

        self.highest_resonance = 0

        
    ##
    #   Gets data as an np array from an open audio file
    #
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

        # unpack data using pyplot
        self.spectrum, self.freqs, self.t, self.im = plt.specgram(data, Fs=samplerate, NFFT=1024)

        # find highest resonance frequency
        frequencies, power = welch(data, samplerate, nperseg=4096)
        self.highest_resonance = frequencies[np.argmax(power)]

        self.rt60 = self.find_average_rt60()

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
    
    ##
    #   Finds the nearest frequency greater than target
    #
    def find_target_frequency(self, target):
        for i in self.freqs:
            if i > target:
                break

        return i
    
    ##
    #   Returns data in DECIBELS from a given audio data input and frequency
    #
    def frequency_data_db(self, frequency):
        freq_to_find = self.find_target_frequency(frequency)
        index = np.where(self.freqs == freq_to_find)[0][0]

        freq_data = self.spectrum[index]

        convert_to_db = 10 * np.log10(freq_data, where=0 < freq_data)

        return convert_to_db
    
    ##
    #   Find the reverberation time in decibels given a reduction value in db and the 
    #   frequency to find the reduction for
    #
    def find_reverb_time(self, reduction_db, frequency):
        data_db = self.frequency_data_db(frequency)
        
        highest_db_index = np.argmax(data_db)
        highest_db_val = data_db[highest_db_index]

        sliced_db = data_db[highest_db_index:]
        
        # finding the value by an offset (which is 5 currently) for a more accurate solution
        offset = 5
        highest_db_val_offset = Model.find_nearest(sliced_db, highest_db_val - offset)
        highest_db_index_offset = np.where(data_db == highest_db_val)

        # looking for the nearest db drop equal to reduction_db
        first_reduction = highest_db_val - (reduction_db + offset)
        first_reduction = Model.find_nearest(sliced_db, first_reduction)

        first_reduction_index = np.where(data_db == first_reduction)
        
        return (self.t[highest_db_index_offset] - self.t[first_reduction_index])[0]
    
    ##
    #   finds the average rt20 then multilies by 3, getting the rt60
    #
    def find_average_rt60(self):
        temp = 0
        for i in self.rt60_freqs:
            temp += self.find_reverb_time(20, i)
        
        avg_rt20 = temp / len(self.rt60_freqs)
        return abs(avg_rt20 * 3)


    ##
    #   Static method to find the nearest value in any integer array
    #
    @staticmethod
    def find_nearest(arr, target):
        np_arr = np.asarray(arr)
        np_arr = np.abs(np_arr - target)
        min_index = np_arr.argmin()

        return arr[min_index]

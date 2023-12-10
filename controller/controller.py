import os
from tkinter import filedialog


class Controller:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    ##
    #   returns file given user input
    #
    def prompt_audio_file(self):
        try:
            input = filedialog.askopenfile(mode='r')
        
        except FileNotFoundError:
            os.error('Incorrect File Given')
        
        filename = input.name
        is_wav = filename.endswith('.wav')

        if not is_wav:
            input = self.model.convert_to_wav(input)
        
        self.model.update(input)
        return input

    def get_specgram(self):
        return self.model.specgram

    def get_data(self):
        return self.model.data

    def get_length_s(self):
        return self.model.t[-1]

    def get_frequency_data_db(self, frequency):
        return self.model.frequency_data_db(frequency)

    def get_time(self):
        return self.model.t


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

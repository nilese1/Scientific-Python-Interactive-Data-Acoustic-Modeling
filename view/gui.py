import tkinter as tk
from controller.controller import Controller
# for testing purposes
from model.model import Model


class View():
    def __init__(self, master=None):
        rootFrame = master
        self.controller = None

        mainFrame = tk.Frame(rootFrame)
        mainFrame.pack()

        loadAudioBtnFrame = tk.Button(mainFrame, text="Load Audio File", command=self.load_button)
        loadAudioBtnFrame.grid(row=0, column=0)

        seconds = tk.StringVar(value="Placeholder")

        secondsLabel = tk.Label(mainFrame, textvariable=seconds)
        secondsLabel.grid(row=1, column=1)


        # loadAudioBtnFrame.pack()
    
    def load_button(self):
        if self.controller:
            self.controller.prompt_audio_file()

    def set_controller(self, controller):
        self.controller = controller




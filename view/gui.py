import tkinter as tk
from controller.controller import Controller
from view.plot import TkPlot

class View():
    def __init__(self, master=None, controller=None):
        rootFrame = master
        self.controller = controller

        mainFrame = tk.Frame(rootFrame)
        mainFrame.pack()
        

        # load audio file
        loadAudioBtnFrame = tk.Button(mainFrame, text="Load Audio File", command=self.load_button)
        loadAudioBtnFrame.grid(row=0, column=0)

        self.seconds = tk.StringVar(value="No file loaded")

        secondsLabel = tk.Label(mainFrame, textvariable=self.seconds)
        secondsLabel.grid(row=1, column=0)
        

        # plot waveform buttons
        waveform_frame = tk.Frame(mainFrame)

        self.waveform_graph = TkPlot(master=waveform_frame)
        waveform_display_button = tk.Button(waveform_frame, text='Load Waveform', command=self.display_waveform)
        waveform_destroy_button = tk.Button(waveform_frame, text='Destroy Waveform', command=self.waveform_graph.destroy)
        
        waveform_frame.grid(row=0, column=2)
        waveform_display_button.pack()
        waveform_destroy_button.pack()
    
    def load_button(self):
        if not self.controller:
            print('No controller loaded??? (whaaat???)')
            return
        
        self.controller.prompt_audio_file()
        self.seconds.set(f'loaded file that is {round(self.controller.get_time(), 2)} seconds long')
    
    def display_waveform(self):
        data = self.controller.get_data()
        self.waveform_graph.update(y=data)

        self.waveform_graph.display()

    def set_controller(self, controller):
        self.controller = controller





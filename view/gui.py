import tkinter as tk
from controller.controller import Controller
from view.plot import TkPlot

class View():
    def __init__(self, master=None, controller=None):
        rootFrame = master

        master.title("Scientific Python Interactive Data Acoustic Modeling")
        master.resizable(width=False, height=False)
        master.geometry("560x400")

        self.controller = controller

        mainFrame = tk.Frame(rootFrame)
        mainFrame.grid(row=0, column=0, padx=10)

        buttonFrame = tk.Frame(mainFrame)
        buttonFrame.grid(row=0, column=0)
        

        # load audio file
        loadAudioBtn = tk.Button(buttonFrame, text="Load Audio File", command=self.load_button)
        loadAudioBtn.grid(row=0, column=0, pady=60)

        self.seconds = tk.StringVar(value="No file loaded")
        

        # plot waveform buttons
        waveform_frame = tk.Frame(mainFrame)
        waveform_frame.grid(row=0, column=1, padx=40)
        waveform_frame.config(bg="white")

        secondsLabel = tk.Label(waveform_frame, textvariable=self.seconds)
        secondsLabel.grid(row=0, column=0, pady=10)
        secondsLabel.config(font=("Arial", 14), bg="white")

        self.waveform_graph = TkPlot(master=waveform_frame)
        waveform_display_button = tk.Button(buttonFrame, text='Load Waveform', command=self.display_waveform)
        waveform_destroy_button = tk.Button(buttonFrame, text='Destroy Waveform', command=self.waveform_graph.destroy)

        waveform_display_button.grid(row=1, column=0, pady=10)
        waveform_destroy_button.grid(row=2, column=0, pady=10)
    
    def load_button(self):
        if not self.controller:
            print('No controller loaded??? (whaaat???)')
            return
        
        self.controller.prompt_audio_file()
        self.seconds.set(f'Duration: {round(self.controller.get_time(), 2)} seconds')
    
    def display_waveform(self):
        data = self.controller.get_data()
        self.waveform_graph.update(y=data)

        self.waveform_graph.display()

    def set_controller(self, controller):
        self.controller = controller





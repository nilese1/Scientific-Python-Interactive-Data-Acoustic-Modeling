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

        rt60Low_frame = tk.Frame(mainFrame)

        self.rt60Low_graph = TkPlot(master=rt60Low_frame)
        rt60Low_display_button = tk.Button(rt60Low_frame, text='Load RT60 Low Graph',
                                    command=self.get_plot_rt60_low)
        rt60Low_frame.grid(row=0, column=3)
        rt60Low_display_button.pack()

        rt60Mid_frame = tk.Frame(mainFrame)

        self.rt60Mid_graph = TkPlot(master=rt60Mid_frame)
        rt60Mid_display_button = tk.Button(rt60Mid_frame, text='Load RT60 Mid Graph',
                                    command=self.get_plot_rt60_mid)
        rt60Mid_frame.grid(row=1, column=3)
        rt60Mid_display_button.pack()

        rt60High_frame = tk.Frame(mainFrame)

        self.rt60High_graph = TkPlot(master=rt60High_frame)
        rt60High_display_button = tk.Button(rt60High_frame, text='Load RT60 High Graph',
                                    command=self.get_plot_rt60_high)
        rt60High_frame.grid(row=2, column=3)
        rt60High_display_button.pack()
    
    def load_button(self):
        if not self.controller:
            print('No controller loaded??? (whaaat???)')
            return
        
        self.controller.prompt_audio_file()
        self.seconds.set(f'loaded file that is {round(self.controller.get_length_s(), 2)} seconds long')
    
    def display_waveform(self):
        data = self.controller.get_data()
        self.waveform_graph.update(y=data)

    def set_controller(self, controller):
        self.controller = controller

    def get_plot_rt60_low(self):
        data = self.controller.get_frequency_data_db(200)
        self.rt60Low_graph.update(x=self.controller.get_time(), y=data)

    def get_plot_rt60_mid(self):
        data = self.controller.get_frequency_data_db(1000)
        self.rt60Mid_graph.update(x=self.controller.get_time(), y=data)

    def get_plot_rt60_high(self):
        data = self.controller.get_frequency_data_db(7500)
        self.rt60High_graph.update(x=self.controller.get_time(), y=data)





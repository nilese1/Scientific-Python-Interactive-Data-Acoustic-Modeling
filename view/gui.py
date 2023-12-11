import tkinter as tk
from controller.controller import Controller
from view.plot import TkPlot

class View():
    def __init__(self, master=None, controller=None):
        rootFrame = master

        master.title("Scientific Python Interactive Data Acoustic Modeling")
        master.resizable(width=False, height=False)
        master.geometry("680x400")

        self.controller = controller

        mainFrame = tk.Frame(rootFrame)
        mainFrame.grid(row=0, column=0, padx=10)

        buttonFrame = tk.Frame(mainFrame)
        buttonFrame.grid(row=0, column=0)
        

        # load audio file
        loadAudioBtn = tk.Button(buttonFrame, text="Load Audio File", command=self.load_button)
        loadAudioBtn.grid(row=0, column=0, pady=60)

        self.display_data = tk.StringVar(value="No file loaded")
        

        # plot waveform buttons
        waveform_frame = tk.Frame(mainFrame)
        waveform_frame.grid(row=0, column=1, padx=40)
        waveform_frame.config(bg="white")

        dataLabel = tk.Label(waveform_frame, textvariable=self.display_data)
        dataLabel.grid(row=0, column=0, pady=10)
        dataLabel.config(font=("Arial", 14), bg="white")

        self.waveform_graph = TkPlot(master=waveform_frame)

        waveform_display_button = tk.Button(buttonFrame, text='Load Plot', command=self.display_waveform)
        waveform_display_button.grid(row=1, column=0, pady=10)

        self.plotMode = tk.IntVar(buttonFrame, 1)
        # Setup radio buttons
        values = {"Waveform": 1,
                  "RT60 Low": 2,
                  "RT60 Mid": 3,
                  "RT60 High": 4}
        i = 2
        for (text, value) in values.items():
            tk.Radiobutton(buttonFrame, text=text, variable=self.plotMode,
                        value=value).grid(row=i, column=0, pady=5)
            i += 1

        self.fileLoaded = False

        # Consolidated plots into radio button

        #rt60Low_frame = tk.Frame(mainFrame)

        #self.rt60Low_graph = TkPlot(master=rt60Low_frame)
        #rt60Low_display_button = tk.Button(rt60Low_frame, text='Load RT60 Low Graph', command=self.get_plot_rt60_low)
        #rt60Low_frame.grid(row=0, column=3)
        #rt60Low_display_button.grid()

        #rt60Mid_frame = tk.Frame(mainFrame)

        #self.rt60Mid_graph = TkPlot(master=rt60Mid_frame)
        #rt60Mid_display_button = tk.Button(rt60Mid_frame, text='Load RT60 Mid Graph',
        #                            command=self.get_plot_rt60_mid)
        #rt60Mid_frame.grid(row=1, column=3)
        #rt60Mid_display_button.grid()

        #rt60High_frame = tk.Frame(mainFrame)

        #self.rt60High_graph = TkPlot(master=rt60High_frame)
        #rt60High_display_button = tk.Button(rt60High_frame, text='Load RT60 High Graph',
        #                            command=self.get_plot_rt60_high)
        #rt60High_frame.grid(row=2, column=3)
        #rt60High_display_button.grid()
    
    def load_button(self):
        if not self.controller:
            print('No controller loaded??? (whaaat???)')
            return
        
        self.controller.prompt_audio_file()
        self.display_data.set(f'File Duration: {round(self.controller.get_length_s(), 2)} seconds\n' +
                              f'Resonance Frequency: {round(self.controller.get_resonance(), 2)} Hz\n' +
                              f'Difference: {self.controller.get_rt60() - .5} s')

        self.fileLoaded = True

    
    def display_waveform(self):
        if not self.fileLoaded:
            return

        x, y = self.controller.get_plot(self.plotMode.get())
        if self.plotMode.get() == 1:
            self.waveform_graph.update(y=y)
        else:
            self.waveform_graph.update(x=x, y=y)

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





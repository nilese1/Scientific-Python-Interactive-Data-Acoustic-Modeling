import tkinter as tk
from controller.controller import Controller
from view.plot import TkPlot

class View():
    def __init__(self, master=None, controller=None):
        rootFrame = master

        master.title("Scientific Python Interactive Data Acoustic Modeling")
        master.resizable(width=False, height=False)
        master.geometry("1920x1000")

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

        rt60Low_frame = tk.Frame(mainFrame)

        self.rt60Low_graph = TkPlot(master=rt60Low_frame)
        rt60Low_display_button = tk.Button(rt60Low_frame, text='Load RT60 Low Graph',
                                    command=self.get_plot_rt60_low)
        rt60Low_frame.grid(row=0, column=3)
        rt60Low_display_button.grid()

        rt60Mid_frame = tk.Frame(mainFrame)

        self.rt60Mid_graph = TkPlot(master=rt60Mid_frame)
        rt60Mid_display_button = tk.Button(rt60Mid_frame, text='Load RT60 Mid Graph',
                                    command=self.get_plot_rt60_mid)
        rt60Mid_frame.grid(row=1, column=3)
        rt60Mid_display_button.grid()

        rt60High_frame = tk.Frame(mainFrame)

        self.rt60High_graph = TkPlot(master=rt60High_frame)
        rt60High_display_button = tk.Button(rt60High_frame, text='Load RT60 High Graph',
                                    command=self.get_plot_rt60_high)
        rt60High_frame.grid(row=2, column=3)
        rt60High_display_button.grid()
    
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





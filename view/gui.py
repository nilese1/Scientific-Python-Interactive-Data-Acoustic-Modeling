import tkinter as tk
import controller.controller as control


class View():
    def __init__(self, master=None):
        rootFrame = master
        mainFrame = tk.Frame(rootFrame)
        mainFrame.pack()

        loadAudioBtnFrame = tk.Button(mainFrame, text="Load Audio File", command=control.LoadFilePressed)
        loadAudioBtnFrame.grid(row=0, column=0)

        seconds = tk.StringVar(value="Placeholder")

        secondsLabel = tk.Label(mainFrame, textvariable=seconds)
        secondsLabel.grid(row=1, column=1)


        # loadAudioBtnFrame.pack()

def start():
    rootFrame = tk.Tk()

    view = View(rootFrame)

    rootFrame.mainloop()


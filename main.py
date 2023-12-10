from view.gui import View
from model.model import Model
from controller.controller import Controller
import tkinter as tk


# for testing purposes only
def start():
    rootFrame = tk.Tk()

    model = Model()
    controller = Controller(model)
    view = View(rootFrame)
    controller.set_view(view)
    view.set_controller(controller)
    
    controller.prompt_audio_file() 

    # test to find RT60
    rt20 = model.find_reverb_time(20, 1000)
    print(f'the rt60 is {rt20*3}')

    rootFrame.mainloop()

start()

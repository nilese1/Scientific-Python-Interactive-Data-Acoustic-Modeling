from view.gui import View
import model.model as mdl
from controller.controller import Controller
import tkinter as tk


# for testing purposes only
def start():
    rootFrame = tk.Tk()
    
    view = View(rootFrame)
    model = mdl.Model()
    controller = Controller(model, view)
    view.set_controller(controller)

    rootFrame.mainloop()

start()

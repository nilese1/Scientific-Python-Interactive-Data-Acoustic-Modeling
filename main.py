from view.gui import View
from model.model import Model
from controller.controller import Controller
import tkinter as tk


# for testing purposes only
def start():
    rootFrame = tk.Tk()
    
    view = View(rootFrame)
    model = Model()
    controller = Controller(model, view)
    view.set_controller(controller)

    rootFrame.mainloop()

start()

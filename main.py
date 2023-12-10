from view.gui import View
import model.model as mdl
from controller.controller import Controller
import tkinter as tk


# for testing purposes only
def start():
    rootFrame = tk.Tk()

    model = mdl.Model()
    controller = Controller(model)
    view = View(rootFrame, controller)
    controller.set_view(view)
    view.set_controller(controller)

    rootFrame.mainloop()

start()

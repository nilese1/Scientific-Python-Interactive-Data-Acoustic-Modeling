from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class TkPlot:
    def __init__(self, master=None, x=None, y=[], sizex_in=5.0, sizey_in=3.0, labelx=None, labely=None):
        self.master = master

        self.x = x
        self.y = y
    
        # main graph + widgets
        self.graph = Figure(figsize=(sizex_in, sizey_in), dpi=100)
        self.graph1 = self.graph.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.graph, master=self.master)
        self.display()

    def display(self):
        self.canvas.get_tk_widget().destroy()

        if self.x is not None:
            self.graph1.plot(self.x, self.y)
        else:
            self.graph1.plot(self.y)
        
        self.canvas = FigureCanvasTkAgg(self.graph, master=self.master) # reinstates canvas to save memory
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0)

    ##
    #   updates the coordinates and redisplays itself
    #
    def update(self, x=None, y=[], reset=True):
        self.x = x
        self.y = y

        # Reset graph so they're not layered on top of eachother
        if reset:
            self.graph = Figure(figsize=(3.5, 3), dpi=100)
            self.graph1 = self.graph.add_subplot(111)

        self.display()

    def stack_plots(self, inputs):
        self.graph = Figure(figsize=(3.5, 3), dpi=100)
        self.graph1 = self.graph.add_subplot(111)
        for i in inputs:
            self.update(x=i[0], y=i[1], reset=False)


    def destroy(self):
        self.canvas.get_tk_widget().destroy()


# def test():
#     y = [i**2 for i in range(100)]
#
#     root = tk.Tk()
#     graph = tkPlot(master=root, y=y)
#     graph_button = tk.Button(master=root, command=graph.display, text='Display Plot', width=10)
#     destroy_button = tk.Button(master=root, command=graph.destroy, text='Destroy Plot', width=10)
#     
#     graph_button.pack()
#     destroy_button.pack()
#
#     root.mainloop()
#
# test()

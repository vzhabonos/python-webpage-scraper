import tkinter as tk


class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


root = tk.Tk()
App(root).pack(side="top", fill="both", expand=True)
root.mainloop()
import tkinter as tk


class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('HTML web page scraper')
        self.label = tk.Label(parent, text='Lorem ipsum dolor sit amet')
        self.label.pack()
        self.create_copy_button()

    def create_copy_button(self):
        self.copy_button = tk.Button(self.parent);
        self.copy_button['text'] = 'Start'
        self.copy_button['command'] = self.copy_button_clicked
        self.copy_button.pack()

    def copy_button_clicked(self):
        if self.label['text'] != 'S U C C':
            self.label['text'] = 'S U C C'
        else:
            self.label['text'] = 'W U T'


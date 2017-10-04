import tkinter as tk
from tkinter import messagebox
from parser import Parser


class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('HTML web page scraper')
        self.create_input()
        self.create_copy_button()

    def create_input(self):
        self.input_label = tk.Label(text="Enter URL for parsing: ")
        self.input_label.pack()
        self.input = tk.Entry()
        self.input.pack()
        self.create_log_window()

    def create_copy_button(self):
        self.copy_button = tk.Button(self.parent);
        self.copy_button['text'] = 'Start'
        self.copy_button['command'] = self.copy_button_clicked
        self.copy_button.pack()

    def create_log_window(self):
        self.log_widget = tk.Text()
        self.log_widget.configure(state=tk.DISABLED)
        self.log_widget.pack()

    def write_log(self, text):
        self.log_widget.configure(state=tk.NORMAL)
        self.log_widget.insert(tk.END, "\n")
        self.log_widget.insert(tk.END, text)
        self.log_widget.see(tk.END)
        self.log_widget.configure(state=tk.DISABLED)

    def show_error_message(self, message):
        messagebox.showerror('Error!', message)

    def copy_button_clicked(self):
        parser = Parser()
        url = self.input.get()
        parser.set_url(url)
        try:
            content = parser.get_content()
            
        except Exception as e:
            self.write_log(e)
            self.show_error_message(e)



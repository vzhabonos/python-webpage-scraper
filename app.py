import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from parser import Parser
from file_helper import FileHelper


class App(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('HTML web page scraper')
        self.create_input()
        self.create_file_input()
        self.create_select_dir_button()
        self.create_copy_button()

    def create_input(self):
        self.input_label = tk.Label(text="Enter URL for parsing: ")
        self.input_label.pack()
        self.url = tk.StringVar();
        self.input = tk.Entry(textvariable=self.url)
        self.input.pack()
        self.create_log_window()

    def create_file_input(self):
        self.file_input_label = tk.Label(text="Choose directory for storing files: ")
        self.file_input_label.pack()
        self.directory = tk.StringVar();
        self.file_input = tk.Entry(textvariable=self.directory)
        self.file_input['state'] = tk.DISABLED
        self.file_input.pack()

    def create_select_dir_button(self):
        self.select_dir_button = tk.Button(self.parent);
        self.select_dir_button['text'] = 'Select directory'
        self.select_dir_button['command'] = self.select_directory
        self.select_dir_button.pack()


    def select_directory(self):
        self.select_dir_button['text'] = 'Selecting...'
        self.select_dir_button['state'] = tk.DISABLED
        self.file_input['state'] = tk.NORMAL
        directory = filedialog.askdirectory(initialdir='.')
        self.directory.set(directory)
        self.file_input['state'] = tk.DISABLED
        self.select_dir_button['text'] = 'Select directory'
        self.select_dir_button['state'] = tk.NORMAL

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
        self.copy_button['text'] = 'Loading...'
        self.copy_button['state'] = tk.DISABLED
        parser = Parser()
        url = self.url.get()
        directory = self.directory.get()
        if FileHelper.directory_exists(directory):
            parser.set_url(url)
            try:
                content = parser.get_content()
                print(content)
                self.write_log("Received HTML page from " + url)
            except Exception as e:
                self.write_log(e)
                self.show_error_message(e)
        else:
            self.write_log("Directory '" + directory + "' not exists")
            self.show_error_message("Directory '" + directory + "' not exists")


        self.copy_button['text'] = 'Start'
        self.copy_button['state'] = tk.NORMAL

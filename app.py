import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from parser import Parser
from file_helper import FileHelper


class App(tk.Frame):

    # Used for determining structure of copied web page
    css_path = '/css/'
    js_path = '/js/'

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
        self.url = tk.StringVar()
        self.input = tk.Entry(textvariable=self.url)
        self.input.pack()
        self.create_log_window()

    def create_file_input(self):
        self.file_input_label = tk.Label(text="Choose directory for storing files: ")
        self.file_input_label.pack()
        self.directory = tk.StringVar()
        self.file_input = tk.Entry(textvariable=self.directory)
        self.file_input['state'] = tk.DISABLED
        self.file_input.pack()

    def create_select_dir_button(self):
        self.select_dir_button = tk.Button(self.parent)
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
        self.copy_button = tk.Button(self.parent)
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
        messagebox.showerror('ERROR', message)

    # Main function for all process of parsing
    def copy_button_clicked(self):
        self.copy_button['text'] = 'Loading...'
        self.copy_button['state'] = tk.DISABLED
        parser = Parser()
        url = self.url.get()
        directory = self.directory.get()
        css_directory = directory + self.css_path
        js_directory = directory + self.js_path
        if FileHelper.directory_exists(directory):
            parser.set_url(url)
            try:
                content = parser.get_content()
                self.write_log("Received HTML page from " + url)
                FileHelper.create_file('index.html', directory, content.decode('utf-8'))
                self.write_log("Saved HTML page to " + directory + '/index.html')
                FileHelper.create_path_recursively(css_directory)
                self.write_log("Created directory for saving CSS stylesheets")
                FileHelper.create_path_recursively(js_directory)
                self.write_log("Created directory for saving JS scripts")

                link_nodes = parser.get_nodes('link')
                for node in link_nodes:
                    link = url + node.get('href')
                    print(link)


            except Exception as e:
                self.write_log("ERROR")
                self.show_error_message(e)
        else:
            self.write_log("ERROR")
            self.show_error_message("Directory '" + directory + "' not exists")
        self.copy_button['text'] = 'Start'
        self.copy_button['state'] = tk.NORMAL

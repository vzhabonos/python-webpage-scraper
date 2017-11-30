import tkinter as tk
from app import App

root = tk.Tk()
App(root).pack(side="top", fill="both", padx=10, pady=20, expand=True)
root.mainloop()
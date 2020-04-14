import tkinter as tk
from tkinter import ttk, messagebox
mainfrm = tk.Tk()
mainfrm.geometry("300x200")
def msg():
    tk.messagebox.showwarning("Warning", "Out of memory")

btn = ttk.Button(mainfrm, text="Click", command=msg, width=10)
btn.pack(padx=20, pady=30)

mainfrm.mainloop()

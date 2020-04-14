import tkinter as tk
from tkinter import ttk

mainfrm = tk.Tk()
ttk.Frame(height=250, width=500).pack()

# สร้างออบเจ็ค
imgSave = tk.PhotoImage(file="Images/delivery.png")
imgPrinter = tk.PhotoImage(file="Images/products.png")

# อ้างอิงชื่อออบเจ็คและเพิ่มออปชัน image สำหรับการแสดงผล
ttk.Label(mainfrm, image=imgSave).place(x=10, y=20)
ttk.Label(mainfrm, image=imgPrinter).place(x=250, y=20)

mainfrm.mainloop()
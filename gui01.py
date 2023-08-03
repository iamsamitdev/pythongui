from tkinter import *  # โหลด module tkinter เข้ามายังโปรแกรม

mainFrm = Tk()  # สร้าง Object ชื่อ mainFrm
mainFrm.title("การเขียนโปรแกรม GUI ด้วยภาษาไพธอน")   # แสดงข้อความที่ title bar
# mainFrm.geometry("300x200+100+200")  # กำหนดความกว้าง สูง ระยะห่างแกน x ระยะห่างแกน y

mainFrm.resizable(False, False)  # This code helps to disable # windows from resizing
window_height = 500
window_width = 900

screen_width = mainFrm.winfo_screenwidth()
screen_height = mainFrm.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

mainFrm.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")


mainFrm.mainloop()  # คำสั่งแสดงผลหน้า GUI
from tkinter import *


root = Tk()
root.title('Схема зала')
root.geometry('800x400')

frame1 = Frame(root)
frame2 = Frame(root)
frame1.pack(pady=10 )
frame2.pack()

screen = Label(frame1, text='Экран')
screen.pack()
canvas = Canvas(frame1, width=400, height=60)
canvas.pack()

canvas.create_line(50, 10, 350, 10, width=8, fill='light blue')
canvas.create_line(60,40, 140, 40, width=4, fill='red')
canvas.create_text(100, 30, text='1000')
canvas.create_line(160,40, 240, 40, width=4, fill='blue')
canvas.create_text(200, 30, text='1100')
canvas.create_line(260,40, 340, 40, width=4, fill='yellow')
canvas.create_text(300, 30, text='1200')





root.mainloop()
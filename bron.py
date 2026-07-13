from tkinter import *


def handler(x):
    btns[x - 1].config(bg='light gray')


def free_(event, nm, row):
    print(event)
    if row <= 2:
        color = 'red'
    elif row >= 3 and row <= 6:
        color = 'blue'
    else:
        color = 'yellow'
    btns[nm - 1].config(bg=color)

root = Tk()
root.title('Схема зала')
root.geometry('800x400')
frame = Frame(root)
frame.pack()
frame1 = Frame(frame)
# frame1.config(bg='lightgrey')
frame2 = Frame(frame)
frame1.pack(pady=10, padx=40)
frame2.pack()

free = Label(frame1, text=' ' * 14)
free.grid(row=0, column=0)

screen = Label(frame1, text='Экран')
screen.grid(row=0, column=1)

canvas = Canvas(frame1, width=400, height=60)
canvas.grid(row=1, column=1)

canvas.create_line(50, 10, 350, 10, width=8, fill='light blue')
canvas.create_line(60, 40, 140, 40, width=4, fill='red')
canvas.create_text(100, 30, text='1200')
canvas.create_line(160, 40, 240, 40, width=4, fill='blue')
canvas.create_text(200, 30, text='1100')
canvas.create_line(260, 40, 340, 40, width=4, fill='yellow')
canvas.create_text(300, 30, text='1000')

row = 10
column = 18
btns = []
for i in range(row):
    row_ = Label(frame2, text=f'Ряд №{i + 1}')
    row_.grid(row=i, column=0)
    for j in range(column):
        num = i * column + j + 1

        if i <= 2:
            color = 'red'
        elif i >= 3 and i <= 6:
            color = 'blue'
        else:
            color = 'yellow'

        btn = Button(frame2)
        btn.config(text=f'{j + 1}', justify=CENTER, font='Arial 10',
                   width=2, bg=color, command=lambda x=num: handler(x))
        btn.grid(row=i, column=j + 1)
        btn.bind('<Button-3>', lambda event, x=num, r=i: free_(event, x, r))
        btns.append(btn)

root.mainloop()

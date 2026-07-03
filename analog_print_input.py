# n = input('ВВедите значение: ')
# print(n)
from tkinter import *


def get_symb():
    item = ent.get().strip()
    out_text.config(text=item)

window = Tk()
inp_text = Label(text='ВВедите значение: ')
inp_text.pack(pady=10)
ent = Entry()
ent.pack()
btn = Button(text='=', command=get_symb)
btn.pack(pady=10)
out_text = Label(text = '           ', bg='lightgrey')
out_text.pack()


window.mainloop()


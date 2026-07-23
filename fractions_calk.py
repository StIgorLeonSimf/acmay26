from tkinter import *
import math


def validator(event):
    # print(event.char)
    entry_text = event.widget.get().strip()
    correct_text = ''.join([t for t in entry_text if t in '0123456789'])
    # print(entry_text, correct_text)
    if entry_text != correct_text:
        event.widget.delete(0, 'end')
        event.widget.insert(0, correct_text)


def validator_oper(event):
    # print(event.char)
    entry_text = oper.get().strip()
    correct_text = ''.join([t for t in entry_text if t in '+-*/'])
    # print(entry_text, correct_text)
    if entry_text != correct_text:
        event.widget.delete(0, 'end')
        event.widget.insert(0, correct_text)


def add(n1, d1, n2, d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d


def sub(n1, d1, n2, d2):
    n = n1 * d2 - n2 * d1
    d = d1 * d2
    return n, d


def mult(n1, d1, n2, d2):
    n = n1 * n2
    d = d1 * d2
    return n, d


def div(n1, d1, n2, d2):
    n = n1 * d2
    d = d1 * n2
    return n, d


def get_items():
    try:
        n1 = int(num1.get())
        d1 = int(den1.get())
        n2 = int(num2.get())
        d2 = int(den2.get())
        znak = oper.get().strip()
    except Exception:
        znak = ''

    match znak:
        case '+':
            n, d = add(n1, d1, n2, d2)
        case '-':
            n, d = sub(n1, d1, n2, d2)
        case '*':
            n, d = mult(n1, d1, n2, d2)
        case '/':
            n, d = div(n1, d1, n2, d2)

    nod = math.gcd(n, d)
    n = n // nod
    d = d // nod
    int_p = ''
    if n > d:
        int_p = n // d
        n = n % d if n % d != 0 else ''
        if not n:
            d = ''
    elif n == d:
        int_p = 1
        n = ''
        d = ''
    elif n == 0 and int_p == '':
        int_p = 0
        n = ''
        d = ''

    int_part['text'] = str(int_p)
    num3['text'] = str(n)
    den3['text'] = str(d)


root = Tk()
root.title('Fractions calculator')
root.geometry('300x150+800+200')

frame = Frame(root)
frame.pack(pady=10)  # в root теперь можно использовать только pack
num1 = Entry(frame, width=2, font=('Arial', 15), justify='center')
num1.grid(row=0, column=0)  # в frame теперь можно использовать только grid
line1 = Label(frame, text=chr(9135) * 5)
line1.grid(row=1, column=0)
den1 = Entry(frame, width=2, font=('Arial', 15), justify='center')
den1.grid(row=2, column=0)

oper = Entry(frame, width=2, font=('Arial', 15), justify='center')
oper.grid(row=1, column=1, padx=5)

num2 = Entry(frame, width=2, font=('Arial', 15), justify='center')
num2.grid(row=0, column=2)
line2 = Label(frame, text=chr(9135) * 5)
line2.grid(row=1, column=2)
den2 = Entry(frame, width=2, font=('Arial', 15), justify='center')
den2.grid(row=2, column=2)

equal = Button(frame, text='=', width=2, command=get_items)
equal.config(font='Arial 15')
equal.grid(row=1, column=3, padx=5)

int_part = Label(frame, text='  ')
int_part.config(font='Arial 20', justify='center', bg='lightgray', width=2)
int_part.grid(row=1, column=4)

num3 = Label(frame, width=2, font=('Arial', 15), justify='center', bg='lightgray')
num3.grid(row=0, column=5)
line3 = Label(frame, text=chr(9135) * 5)
line3.grid(row=1, column=5)
den3 = Label(frame, width=2, font=('Arial', 15), justify='center', bg='lightgray')
den3.grid(row=2, column=5)

num1.bind('<KeyRelease>', validator)
num2.bind('<KeyRelease>', validator)
den1.bind('<KeyRelease>', validator)
den2.bind('<KeyRelease>', validator)
oper.bind('<KeyRelease>', validator_oper)

root.mainloop()

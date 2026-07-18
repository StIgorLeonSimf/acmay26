from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os


def save_image():
    if img_s is None:
        print('Нет изображения')
        return
    default_name = os.path.basename(file_name)
    fp = fd.asksaveasfilename(
        defaultextension='.png',
        initialfile=default_name,
        filetypes=[('PNG files', '*.png'), ('All Files', '*.*')]
    )
    if fp:
        img_s.save(fp)
        print(f'Файл сохранен {fp}')



def open_img():
    url = 'https://cataas.com/cat'

    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


def load_image(url):
    global img_s
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img_s = Image.open(image_data)
        img_s.thumbnail((600, 450),Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img_s)

    except Exception as exc:
        print('Ошибка:', exc)
        return None


img_s = None
file_name = 'cat.png'
root = Tk()
root.geometry('600x500')
root.title('Котики')



label = Label()
label.pack()
btn1 = Button(text='next', command=open_img)
btn1.pack()
btn2 = Button(text='save', command=save_image)
btn2.pack()
open_img()
# img = load_image(url)
# if img:
#     label.config(image=img)
#     label.image = img

root.mainloop()
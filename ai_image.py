import tkinter as tk
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from io import BytesIO
import requests
import os.path
import asyncio
from g4f.client import AsyncClient
from translate import Translator


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


async def gen_url(nm):
    client = AsyncClient()

    response = await client.images.generate(
        prompt=nm,
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")
    return image_url


def open_img():
    nm = text.get().strip()
    nm = translator.translate(nm.capitalize())
    url = asyncio.run(gen_url(nm))
    img = None
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
translator = Translator(from_lang='ru', to_lang='en')

root = tk.Tk()
root.geometry('600x600')
root.title('Котики')
frame1 = tk.Frame(root)
frame1.pack(pady=10)
frame2 = tk.Frame(root)
frame2.pack()

text = tk.Entry(frame1)
text.config(width=40, font='Arial 15')
text.grid(row=0, columnspan=2, pady=5)
text.insert(0, 'Kittes')

btn1 = tk.Button(frame1, text='next', width=10, command=open_img)
btn1.grid(row=1, column=0)
btn2 = tk.Button(frame1, text='save', width=10, command=save_image)
btn2.grid(row=1, column=1)

label = tk.Label(frame2)
label.pack()
open_img()
# img = load_image(url)
# if img:
#     label.config(image=img)
#     label.image = img

root.mainloop()
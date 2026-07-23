import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from  io import BytesIO



def get_random_dog_image():
    try:
        response = requests.get('https://dog.ceo/api/breeds/image/random')
        response.raise_for_status()
        data = response.json()
        return data['message']
    except Exception as err:
        messagebox.showerror('Ошибка', f'Ошибка запроса API {err}')
        return None


def show_image():
    image_url = get_random_dog_image()
    if image_url:
        try:
            response = requests.get(image_url, stream=True)
            response.raise_for_status()
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            size = (int(width_spinbox.get()), int(height_spinbox.get()))
            img.thumbnail(size)
            img = ImageTk.PhotoImage(img)

            new_window = Toplevel()
            new_window.title('Новое окно')
            label = ttk.Label(new_window, image=img)
            label.config(image = img)
            label.image = img
            label.pack(padx=10, pady=10)

        except requests.RequestException as err:
            messagebox.showerror('Ошибка',f'Не удалось загрузить изображение {err}')
    progress.stop()

def prog():
    progress['value'] = 0
    progress.start(20)
    root.after(3000, show_image)


# def spinbox():
#     width = int(width_spinbox.get())
#     height = int(height_spinbox.get())
#     coord = width, height
#     return coord

root = Tk()
root.title("Собачки")
root.geometry('360x420')
label = ttk.Label()
label.pack(padx=10, pady=10)

button = ttk.Button(text='Загрузить изображение', command = prog)
button.pack(padx=10, pady=10)

progress = ttk.Progressbar(mode='determinate', length=300)
progress.pack(padx=10, pady=10)

width_label = ttk.Label(text='Ширина')
width_label.pack(side='left', padx=(10,0))
width_spinbox = ttk.Spinbox(from_= 200, to=500, increment=50, width=5)
width_spinbox.pack(side='left', padx=(0,10))

height_label = ttk.Label(text='Высота')
height_label.pack(side='left', padx=(10,0))
height_spinbox = ttk.Spinbox(from_= 200, to=500, increment=50, width=5)
height_spinbox.pack(side='left', padx=(0,10))


root.mainloop()
from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog as fd
from tkinter import ttk
from datetime import datetime
import json
import os

import requests
import pyperclip

history_file = 'upload_history.json'


def save_history(filepath, download_link):
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    history.append({'file_path': os.path.basename(filepath),
                    'download_link': download_link})
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=4)


def show_history():
    if not os.path.exists(history_file):
        mb.showinfo('История', 'история загрузок пуста')
        return

    history_win = Toplevel(window)
    history_win.title('История загрузок')
    files_listbox = Listbox(history_win, width=50, height=20)
    files_listbox.grid(row=0, column=0, padx=(10, 0), pady=10)
    links_listbox = Listbox(history_win, width=50, height=20)
    links_listbox.grid(row=0, column=1, padx=(0, 10), pady=10)
    with open(history_file, 'r') as f:
        history = json.load(f)
        for item in history:
            files_listbox.insert(END, item['file_path'])
            links_listbox.insert(END, item['download_link'])


def upload():
    try:
        filepath = fd.askopenfilename()
        with open(filepath, 'rb') as file:
            files = {'file': file}
            response = requests.post('https://store1.gofile.io/uploadfile',
                                     files=files)
            response.raise_for_status()
            data = response.json()
            print(data)
            print(datetime.fromtimestamp(data['data']['createTime'])
                  .strftime('%d-%m-%Y %H:%M:%S'))
            download_link = data['data']['downloadPage']

            if download_link:
                entry.delete(0, END)
                entry.insert(0, download_link)
                pyperclip.copy(download_link)
                save_history(filepath, download_link)
                mb.showinfo('Копирование ссылки',
                            f'Ссылка {download_link} скопирована в буфер обмена')
            else:
                raise ValueError('Не удалось получить ссылку для скачивания')

    except ValueError as e:
        mb.showerror("Error", e)
    except Exception as e:
        mb.showerror("Error", e)


window = Tk()
window.title('Сохранение файлов в облаке')
window.geometry('400x200')

upload_button = ttk.Button(text='загрузить файл', command=upload)
upload_button.pack(pady=20)
entry = ttk.Entry(width=50)
entry.pack()
history_button = ttk.Button(text='Просмотреть историю', command=show_history)
history_button.pack(pady=20)

window.mainloop()

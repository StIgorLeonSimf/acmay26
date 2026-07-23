import tkinter as tk

def show_event_info(event):
    info = f"""
    Виджет: {event.widget}
    Координаты (x, y): ({event.x, event.y})
    Координаты экрана (x_root, y_root): ({event.x_root, event.y_root} )
    """
    # события клавиатуры
    if hasattr(event, 'char'):
        info += f'\n Cимвол: "{event.char}"'
        info += f'\n Имя клавиши: "{event.keysym}"'
        info += f'\n Код клавиши: "{event.keycode}"'
    # события мыши
    if hasattr(event, 'num'):
        info += f'\nНомер кнопки: {event.num}'

    print(info)

root = tk.Tk()
frame = tk.Frame(root, width=300, height=300, background='gray')
frame.pack(padx=25, pady=25)
# привяжем одному обработчику разные события
frame.bind('<Button-1>', show_event_info)
frame.bind('<Key>', show_event_info)
frame.focus_set()

root.mainloop()





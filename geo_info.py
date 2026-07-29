from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            # lat = round(results[0]['geometry']['lat'], 2)
            lat = results[0]['geometry']['lat']
            # lon = round(results[0]['geometry']['lng'], 2)
            lon = results[0]['geometry']['lng']
            country = results[0]['components']['country']
            osm_url = f'https://www.openstreetmap.org/?mlat={lat}&mlon={lon}'
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']

                return {"coordinates": f'Широта: {lat}, Долгота: {lon}\n'
                        f'Страна: {country}\n Регион: {region}',
                        "map_url": osm_url}
            else:
                return {"coordinates": f'Широта: {lat}, Долгота: {lon}\n'
                        f'Страна: {country}',
                        "map_url": osm_url}


        else:
            return f'Город {city} не найден, map_url: None'
    except Exception as e:
        print(f'Ошибка: {e}, map_url: None')

def show_coordinates(event=None):
    city = entry.get().strip()
    result = get_coordinates(city, apikey)
    label.config(text=result["coordinates"])
    global map_url
    map_url = result['map_url']

def show_map():
    if map_url:
        webbrowser.open(map_url)



window = Tk()
window.title('Поиск координат города')
map_url = None
apikey = '96112fb6d80d4059ae9dabea94898600'

entry = Entry(window, width=30)
entry.pack()

label = Label(window, text='Введите название города и нажмите кнопку "Получить"')
label.pack()
button = Button(text="Получить", command=show_coordinates)
button.pack()
entry.bind("<Return>", show_coordinates)

map_button = Button(text='Показать карту', command=show_map)
map_button.pack()

window.mainloop()









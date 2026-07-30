from bottle import response
from opencage.geocoder import OpenCageGeocode
from tkinter import *
import webbrowser
import requests


def get_weather(lat, lon):

    try:
        url = (f'https://api.open-meteo.com/v1/forecast?latitude='
              f'{lat}&longitude={lon}&current_weather=true')
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        print(weather_data)
        current_weather = weather_data['current_weather']
        return current_weather
    except Exception as e:
        return f'Ошибка при получении погоды: {e}'

def show_weather():
    current_weather = get_weather(lat, lon)
    print(current_weather)

    weather_window = Toplevel(window)
    weather_window.title('Погода сейчас')
    weather_window.geometry('350x100+400+300')


    if isinstance(current_weather, str):
        label = Label(weather_window, text=current_weather)
    else:
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        weather_text = (f'Температура: {temperature}{chr(176)}C\n'
                        f'Cкорость ветра: {windspeed} km/h\n')
        label = Label(weather_window, text=weather_text)
        label.pack(pady=10)


def get_coordinates(city, key):
    global lat, lon
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
window.geometry('350x210+200+200')
map_url = None
lat = None
lon = None
apikey = '96112fb6d80d4059ae9dabea94898600'

entry = Entry(window, width=30)
entry.pack(pady=10)

label = Label(window, text='Введите название города и нажмите кнопку "Получить"')
label.pack()
button = Button(text="Получить", command=show_coordinates)
button.pack(pady=10)
entry.bind("<Return>", show_coordinates)

map_button = Button(text='Показать карту', command=show_map)
map_button.pack()
weather_button = Button(text='Показать погоду', command=show_weather)
weather_button.pack(pady=10)

window.mainloop()









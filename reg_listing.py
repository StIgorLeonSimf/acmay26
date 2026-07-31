import requests
import re


def  validate_phone_number(phone_number):
       # pattern = r'^\d{11}$'
       # pattern = r'^[79]\d{10}$'
       pattern = r'^79\d{9}$'
       # print(re.findall(pattern, phone_number))
       # exit(0)
       return bool(re.match(pattern, phone_number))


user = 'Igor'
password = 'Ig123@com'
sender = 'Отправитель'
receiver = '79781962001'
text = 'TEST 1234567890'
url = (f'https://my3.webcom.mobi/sendsms.php?user={user}'
       f'&pwd={password}&sadr={sender}&dadr={receiver}'
       f'&text={text}')
if not validate_phone_number(receiver):
       print(f'Номер телефона {receiver} некорректен!!!')
       exit(0)
try:

       response = requests.get(url)
       response.raise_for_status()
       if response.status_code == 200:
              print('Успешно отправлено!')
       # else:
       #        print('Ошибка:', response.status_code)
except Exception as e:
       print('Ошибка:', e)
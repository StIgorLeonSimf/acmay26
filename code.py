with open('text.txt', encoding='utf-8') as fl:
    s = fl.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for symbol in s:
        code = ord(symbol) + int(key)
        smble = chr(code)
        secret += smble
    print(f'Текст зашифрован..')

with open('code.txt', 'w', encoding='utf-8') as fl:
    fl.write(secret)
print('Файл code.txt к отправке подготовлен!')
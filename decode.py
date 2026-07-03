with open('code.txt', encoding='utf-8') as fl:
    s = fl.read()
    key = input('Введите ключ шифрования: ')
    secret = ''
    for symbol in s:
        code = ord(symbol) - int(key)
        smble = chr(code)
        secret += smble
    print(f'Текст расшифрован..')

with open('decode.txt', 'w', encoding='utf-8') as fl:
    fl.write(secret)
print('Файл decode.txt cформирован!')
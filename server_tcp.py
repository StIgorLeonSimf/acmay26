import socket

# Параметры подключения

IP = '127.0.0.1'
port = 9001  # всего 65536 не трогаем до 1024 совсем далее до 8000 не желательно
end_point = (IP, port)

# Сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(end_point)
server.listen(10)

#Переход в режим ожидания запросов от клиентов
print(f'сервер запущен на IP: {IP}\nПорт: {port}')
print('Режим ожидания запросов.')

connection, client_address = server.accept()
# обмен данными
try:
    print(f'Установлено соединение с клиентом: {client_address}')
    while True:
        client_message = connection.recv(1024).decode(encoding='utf-8')
        if client_message == 'stop_server' or not client_message:
            break
        print(f'Сообщение от клиента: [{client_message}]')
        # отправка сообщения
        server_message = input('Ответ сервера: ')
        connection.send(server_message.encode(encoding='utf-8'))
        print('Сообщение отправлено!')
except Exception as e:
    print(e)

finally:
    connection.close()
    print('Сервер остановлен')
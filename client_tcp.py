import socket

IP = '127.0.0.1'
PORT = 9001
END_POINT = (IP, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(END_POINT)
    while True:
        # отправка сообщений
        client_message = input('Сообщение серверу: ')
        client.send(client_message.encode(encoding='utf-8'))
        if client_message == 'stop_server':
            break
        # прием сообщения
        server_message = client.recv(1024).decode(encoding='utf-8')
        print(f'Ответ сервера: {server_message}')

except BaseException as e:
    print(e)
finally:
    client.close()
    print('связь с сервером прервана')

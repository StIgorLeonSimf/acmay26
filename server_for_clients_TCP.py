import socket
import threading


# Параметры подключения

def handle_client(connection, client_address):
    """Обработка одного клиента"""
    # global server
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
            if server_message == 'stop_server_12345':
                server.close()
                break
            connection.send(server_message.encode(encoding='utf-8'))
            print('Сообщение отправлено!')
    except Exception as e:
        print(f'Ошибка обмена с клиентом {client_address} - {e}')

    finally:
        connection.close()
        print(f'Соединение с клиентом: {client_address} прервано')


def start_server():
    global server
    IP = '127.0.0.1'
    PORT = 9001  # всего 65536 не трогаем до 1024 совсем далее до 8000 не желательно
    END_POINT = (IP, PORT)

    # Сокет сервера
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(END_POINT)
    server.listen(10)

    # Переход в режим ожидания запросов от клиентов
    print(f'сервер запущен на IP: {IP}\nПорт: {PORT}')
    print('Режим ожидания запросов.')
    try:
        while True:
            connection, client_address = server.accept()
            client_thread = threading.Thread(
                target=handle_client,
                args=(connection, client_address), daemon=True)
            client_thread.start()
            print(f'Поток для клиента {client_address} запущен!')
    except Exception as err:
        print(f'Ошибка сервера: {err} ')
    finally:
        server.close()


if __name__ == '__main__':
    server = None
    start_server()

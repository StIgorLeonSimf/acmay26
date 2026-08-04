import multiprocessing as mp
import time
import random

def producer(queue, n_items):
    """Производтель: генерация чисел и отправка в очередь"""
    for i in range(n_items):
        item = random.randint(1, 100)
        queue.put(item)
        print(f'Производитель создал число: {item} ')
        time.sleep(random.uniform(.1, .5))
    queue.put(None)


def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        result = item ** 2
        print(f'Получено: {item} => результат: {result}')
        time.sleep(random.uniform(.2, .6))
    print('Пользователь работу завершил')


if __name__ == '__main__':
    q = mp.Queue()
    p_producer = mp.Process(target=producer, args=(q, 10))
    p_consumer = mp.Process(target=consumer, args=(q,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print('Главный процесс завершен!')


















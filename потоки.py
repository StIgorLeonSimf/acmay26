import time
from threading import Thread


def f1(n):
    print(n * 5)
    time.sleep(3)
    print(f'Функция F1 работу закончила')


def f2(n):
    print(n * 2)
    time.sleep(2)
    print(f'Функция F2 работу закончила')


def main():
    thread1 = Thread(target=f1, args=(20,), daemon=True)
    thread2 = Thread(target=f2, args=(100,))
    thread2.daemon = True  # прерывание потока по факту окончания работы процесса
    # f1(100)
    # f2(20)
    thread1.start()
    thread2.start()

    # thread1.join()  # продолжает процесс до окончания работы потока
    # thread2.join()
if __name__ == '__main__':
    start = time.time()
    main()

    stop = time.time()
    print(f'{stop - start:.2f}')
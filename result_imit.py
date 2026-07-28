from Work_threading import WorkThreading
from time import sleep


print('запуск основного потока')
thread1 = WorkThreading(1, '\t',5, 3)
thread2 = WorkThreading(2, '\t\t',5, 2)
thread3 = WorkThreading(3, '\t\t\t',5, 4)

thread1.start()
thread2.start()
thread3.start()
for i in range(5):
    print(f'Основной поток => действие {i + 1}')
    sleep(1)
print('завершение основного потока')
thread1.join()
thread2.join()
thread3.join()





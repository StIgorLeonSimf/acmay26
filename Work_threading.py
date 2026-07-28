from threading import Thread
from time import sleep


class WorkThreading(Thread):
    def __init__(self, num, tab, vol, dur):
        super().__init__()
        self.num = num
        self.tab = tab
        self.vol = vol
        self.dur = dur

    def run(self):
        print(f'Поток {self.num} начал выполнение')
        for k in range(self.vol):
            print(f'{self.tab} Поток - {self.num} => действие{k + 1}')
            sleep(self.dur)
        print(f'Поток {self.num} завершил выполнение')
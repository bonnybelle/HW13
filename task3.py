# Создать менеджер контекста который будет подсчитывать время выполнения блока инструкций
from datetime import datetime
import time


class Manager:
    def __init__(self):
        self.start = datetime.now()
        self.finish = None

    def __enter__(self):
        time.sleep(2)
        self.finish = datetime.now() - self.start
        return 'time spent: {}'.format(self.finish)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


with Manager() as m1:
    print('m1', m1)

with Manager() as m2:
    print('m2', m2)

# Создать менеджер контекста который будет подсчитывать время выполнения блока инструкций
import sys
from datetime import datetime
import time


class Manager:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.start = datetime.now()
        self.finish = None

    def __enter__(self):
        self.res = []
        for i in range(self.first, self.last):
            i *= i+1
            self.res.append(i)
            time.sleep(0.5)
        return self.res

    def __exit__(self):
        self.finish = datetime.now() - self.start
        return '\ntime spent: {}\n'.format(self.finish)


m1 = Manager(0, 9)
m2 = Manager(9, -1)

print('m1:', m1.__enter__(), m1.__exit__(),
      '\nm2:', m2.__enter__(),  m2.__exit__())

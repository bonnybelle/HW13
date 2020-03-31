# Написать декоратор и менеджер контекста который будет подавлять все ошибки возникающие в теле вашей функции.
import sys


def error_decorator(function_to_decorate):
    print('----DECORATOR----')

    def wrapper():
        try:
            res = function_to_decorate()
        except Exception as e:
            res = e
        return res

    return wrapper()


@error_decorator
def my_function():
    i = int(input('value: '))
    return i


print(my_function)


class Manager:
    print('----MANAGER----')

    def __init__(self, value1, value2, action):
        self.value1 = value1
        self.value2 = value2
        self.action = action

    def __enter__(self):
        try:
            self.res = self.action(self.value1, self.value2)
        except Exception as e:
            self.res = e
        return self.res

    def __exit__(self):
        if self.res is Exception:
            print(self.res)
            sys.exit()


m1 = Manager(5, 'asd', lambda a, b: a / b)
m2 = Manager(5, 0, lambda a, b: a / b)
m3 = Manager(5, 2, lambda a, b: a / b)
print('m1:', m1.__enter__(),
      '\nm2:', m2.__enter__(),
      '\nm3:', m3.__enter__())

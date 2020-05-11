# Написать декоратор и менеджер контекста который будет подавлять все ошибки возникающие в теле вашей функции.


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
    i = int('asd')
    return i


print(my_function)


class Manager:
    print('----MANAGER----')

    def __init__(self, *args):
        self.args = args

    def __enter__(self):
        try:
            self.res = self.args[0] / self.args[1]
            return self.res
        except Exception as e:
            self.res = e
            print(e)
        return self.res

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.res is Exception:
            print(self.res)


with Manager(5, 'asd') as m1:
    print()

with Manager(5, 0) as m2:
    print()

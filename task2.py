# Написать декоратор c аргументом который будет подавлять определенные ошибки возникающие в теле вашей функции.
# Ошибки которые должен будет подавить ваш декоратор вы должны передать ему в качестве аргумента


def decorator(error):
    def actual_decorator(function_to_decorate):

        def wrapper():
            try:
                result = function_to_decorate()
            except error:
                result = error
            return result

        return wrapper

    return actual_decorator


@decorator(error=ZeroDivisionError)
def my_function1():
    i = 5/0
    return i


@decorator(error=ValueError)
def my_function2():
    i = int('asd')
    return i


@decorator(error=TypeError)
def my_function3():
    i = 'asd' + 15
    return i


print('my_function1: ', my_function1())
print('my_function2: ', my_function2())
print('my_function3: ', my_function3())

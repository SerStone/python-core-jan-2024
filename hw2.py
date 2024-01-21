# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно
# реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи


# 2) протипізувати перше завдання
from typing import Callable


def daily_organiser() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    massive: list[str] = ['Get up 08:00']

    def add_duty(duty: str) -> None:
        nonlocal massive
        massive.append(duty)

    def print_duties():
        nonlocal massive
        return massive

    return add_duty, print_duties


add_d, print_d = daily_organiser()
print(add_d('Brushed teeth 08:10'))
print(print_d())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки
# (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'


def expanded_form(num: int) -> str:
    return ' + '.join(ch + '0' * (len(str(num)) - 1 - i) for i, ch in enumerate(str(num)) if ch != '0')


print(expanded_form(405))

# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована
# цим декоратором, та буде виводити це значення після виконання функцій


def counter_decorator(fnc):
    counter = 0

    def increment(*args, **kwargs):
        nonlocal counter
        counter += 1
        fnc(*args, **kwargs)
        print(f'Incremented {counter} times')

    return increment


@counter_decorator
def fnc1():
    print('f1')


@counter_decorator
def fnc2():
    print('f2')


fnc1()
fnc1()
fnc2()

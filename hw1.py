# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,

# str = 'as 23 fdfdg544'
#
# def findch(str1):
#     nums = [ch for ch in str1 if ch.isdigit()]
#     print(','.join(nums))
#
# findch(str)
#
# print(','.join([ch for ch in str if ch.isdigit()]))

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написанi

# str = 'as 23 fdfdg544'
#
# print(' '.join(''.join([ch if ch.isdigit() else ' ' for ch in str]).split()))



# list comprehension


# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

# greeting = 'Hello, world'
#
# print([ch.upper() for ch in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

# function

# - створити функцію яка виводить ліст
# list = [1, 2, 3, 4, 5]
#
# def output_list(list):
#     print(list)
#
# output_list(list)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# a, b, c = 3, 4, 5
#
# def max_num(a, b, c):
#    maximal = max(a, b, c)
#    print(maximal)
#
# max_num(a, b, c)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# a, b, c = 3, 4, 5
#
# def max_min_num(a, b, c):
#    maximal = max(a, b, c)
#    minimal = min(a, b, c)
#    print(maximal)
#    return minimal
#
# max_min_num(a, b, c)

# - створити функцію яка повертає найбільше число з ліста

# list = [1, 2, 3, 4, 5]
#
# def max_num_list(list):
#     print(max(list))
#
# max_num_list(list)

# - створити функцію яка повертає найменьше число з ліста

# list = [1, 2, 3, 4, 5]
#
# def min_num_list(list):
#     return min(list)
#
# min_num_list(list)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# list = [1, 2, 3, 4, 5]
#
# def sum_nums(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
#
# print(sum_nums(list))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# list = [1, 2, 3, 4, 5]
#
# def avr_val(list):
#     value = 0
#     for i in list:
#         value += i
#     value = value // len(list)
#     return value
#
#
# print(avr_val(list))

# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
list = [22, 3,5,2,8,2,-23, 8,23,5]

def min_value(list):
    return min(list)

# print(min_value(list))

#   - видалити усі дублікати

# list = [22, 3,5,2,8,2,-23, 8,23,5]
def rm_duplicate(list):
    new_list = set(list)
    return new_list

# print(rm_duplicate(list))

#   - замінити кожне 4-те значення на 'X'

# list = [22, 3,5,2,8,2,-23, 8,23,5]
#
def x_func(list):
    x_list = ['X' if (i + 1) % 4 == 0 else rest for i, rest in enumerate(list)]
    return x_list

# print(x_func(list))

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def draw_square(value):
    for i in range(value):
        if i == 0 or i == value - 1:
            print('* ' * value)
        else:
            print('* ' + '  ' * (value - 2) + '*')



# 3) вывести табличку множення за допомогою цикла while

def mult_tab():
    row = 1

    while row <= 9:
        column = 1
        while column <= 9:
            product = row * column
            print(f"{row} * {column} = {product:2}", end='\t')
            column += 1
        print()
        row += 1



# 4) переробити це завдання під меню

while True:
    print('0. Exit!')
    print('1. Min Value')
    print('2. Remove Duplicate')
    print('3. Replace each 4-th value on X')
    print('4. Draw square by inputting side')
    print('5. Print Multiple Tab')

    choice = input('Your choice: ')

    if choice == '1':
        print(min_value(list))
    elif choice == '2':
        print(rm_duplicate(list))
    elif choice == '3':
        print(x_func(list))
    elif choice == '4':
        draw_square(3)
    elif choice == '5':
        mult_tab()
    elif choice == '0':
        break
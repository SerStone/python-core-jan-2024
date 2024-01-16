# #ДЗ
#
# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

# st = 'as 23 fdfdg544'
#
# print(','.join(lt for lt in st if lt.isdigit()))

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################
#
# st = 'as 23 fdfdg544  34'
#
# print(','.join(''.join([lt if lt.isdigit() else ' ' for lt in st]).split()))


# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
# greeting = 'Hello, world'
#
# print([halo.upper() for halo in greeting])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]
# nums = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324]
#
# print([num**2 for num in nums if num < 50])
#
# function
#
# - створити функцію яка виводить ліст
# lt = [1, 2, 3, -3, 44, 1]
#
# def out_list(list):
#     print([el for el in list])
#
# out_list(lt)
# - створити функцію яка приймає три числа та виводить та повертає найбільше.

# a = b = 6
# c = 33
#
# def find_max(a, b, c):
#     print(max(a, b, c))
#
# find_max(a, b, c)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def find_nums(*args):
#     print(max(args))
#     return min(args)
#
#
# print(find_nums(1, 66, -3))

# - створити функцію яка повертає найбільше число з ліста

# lt = [1, 2, 3, -3, 44, 1]
#
# def find_max(list):
#     return max(list)
#
# print(find_max(lt))

# - створити функцію яка повертає найменьше число з ліста

# lt = [1, 2, 3, -3, 44, 1]
#
# def find_min(list):
#     return min(list)
#
# print(find_min(lt))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# lt = [1, 2, 3, -3, 44, 1]

# def sum_func(list):
#     return sum(list)
#
#
# print(sum_func(lt))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# lt = [1, 2, 3, -3, 44, 1]
#
# def avr_func(list):
#     return sum(list)/len(list)
#
#
# print(avr_func(lt))
#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


def find_min(list):
    print(min(list))


# find_min(list)

#   - видалити усі дублікати

def rm_duplicate(list):
    s = set(list)
    return s


# print(rm_duplicate(list))

#   - замінити кожне 4-те значення на 'X'

def x_func(list):
    print(['X' if (i - 1) % 4 == 0 else el for i, el in enumerate(list)])


# x_func(list)

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square_draw(side):
    for i in range(side):
        if i == 0 or i == side - 1:
            print('* ' * side)
        else:
            print('* ' + '  ' * (side - 2) + '*')
        print()


# print(square_draw(4))
# 3) вывести табличку множення за допомогою цикла while

def mult_tab():
    row = 1
    while row <= 9:
        column = 1
        while column <= 9:
            mult = row * column
            print(f'{row} * {column} = {mult}')
            column += 1
        row += 1
        print()


# mult_tab()

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
        find_min(list)
    elif choice == '2':
        print(rm_duplicate(list))
    elif choice == '3':
        x_func(list)
    elif choice == '4':
        square_draw(5)
    elif choice == '5':
        mult_tab()
    elif choice == '0':
        break

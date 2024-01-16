# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
from itertools import product

# st = 'as 23 fdfdg544'
#
# print(',' .join([lt for lt in st if lt.isdigit()]))
#
# print('-' .join([lt for lt in st if lt.isalpha()]))
# print('-' .join([lt for lt in st if lt.isalnum()]))


# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

# st = 'as 23 fdfdg544 34'
#
# print(','.join(''.join([lt if lt.isdigit() else ' ' for lt in st]).split()))
# #################################################################################
#
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
# print([res**2 for res in nums if res < 50])

#
# function
#
# - створити функцію яка виводить ліст

# l = [1,2,3,4,5,6,7,8,9]

# def list_output(list):
#     print(list)
#
# list_output(l)

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
# z=x=3
# c=5
#
# def find_max(a,b,c):
#     return max(a,b,c)
#
# print(find_max(z,x,c))
# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

# def output_func(*args):
#     print(max(args))
#     return min(args)
#
# print(output_func(1,2,3))

# - створити функцію яка повертає найбільше число з ліста

# l = [1,2,3,4,5,16,7,8,9]
#
# def find_max(list):
#     print(max(list))
#
# find_max(l)
# - створити функцію яка повертає найменьше число з ліста

# l = [1,2,3,4,5,16,7,8,9]
#
# def find_max(list):
#     print(min(list))
#
# find_max(l)

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

# l = [1,2,3,4,5,16,7,8,9]
#
# def sum_func(list):
#     return sum(list)
#
# print(sum_func(l))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

# l = [1,2,3,4,5,16,7,8,9]

# def avr_func(list):
#     return sum(list) / len(list)
#
#
# print(avr_func(l))

#
#
#
#
# ################################################################################################
# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число

list = [22, 3,5,2,8,2,-23, 8,23,5]

def find_min(list):
    min_index = list.index(min(list))
    return list[min_index]

print(find_min(list))

#   - видалити усі дублікати

def rm_duplicates(list):
    s = set(list)
    return s


print(rm_duplicates(list))

#   - замінити кожне 4-те значення на 'X'

def x_replicator(list):
    new_list = ['X' if (i + 1) % 4 == 0 else elem for i, elem in enumerate(list)]
    return new_list


print(x_replicator(list))

# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square_draw(side):
    for i in range(side):
        if i == 0 or i == side - 1:
            print('* ' * side)
        else:
            print('* ' + '  ' * (side - 2) + '*')
square_draw(5)




# 3) вывести табличку множення за допомогою цикла while

# def output_mult_tab():
#     row = 1
#
#     while row <= 9:
#         column = 1
#         while column <= 9:
#             product = row * column
#             print(f'{row} * {column} = {product:2}', end='\t')
#             column += 1
#         print()
#         row += 1

# output_mult_tab()

def output_mult_tab():
    row = 1

    while row <= 9:
        column = 1
        while column <= 9:
            mult = row * column
            print(f'{column} * {row} = {mult:2}', end='\t')
            column += 1
        print()
        row += 1

output_mult_tab()



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
        print(find_min(list))
    elif choice == '2':
        print(rm_duplicates(list))
    elif choice == '3':
        print(x_replicator(list))
    elif choice == '4':
        square_draw(3)
    elif choice == '5':
        output_mult_tab()
    elif choice == '0':
        break


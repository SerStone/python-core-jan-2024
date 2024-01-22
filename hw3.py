# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.area = self.x * self.y

    def __add__(self, other):
        return self.area + other.area

    def __sub__(self, other):
        return self.area - other.area

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __lt__(self, other):
        return self.area < other.area

    def __gt__(self, other):
        return self.area > other.area

    def __len__(self):
        return (self.x + self.y) * 2


rectangle1 = Rectangle(3, 4)
rectangle2 = Rectangle(5, 6)
print('-*-' * 10)
print(f"Area rectangle 1: {rectangle1.area}")
print(f"Area rectangle 2: {rectangle2.area}")

sum_result = rectangle1 + rectangle2
sub_result = rectangle1 - rectangle2
length_result = len(rectangle1)

print(f"Sum areas: {sum_result}")
print(f"Sub areas: {sub_result}")
print(f"eq: {rectangle1 == rectangle2}")
print(f"not eq: {rectangle1 != rectangle2}")
print(f"less than rectangle 2: {rectangle1 < rectangle2}")
print(f"greater than rectangle 2: {rectangle1 > rectangle2}")
print(f"length of rectangle 1: {length_result}")
print('-*-' * 10)
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список
# попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0

    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(cls.__count)

    def __str__(self):
        return str(self.__dict__)


class Prince(Human):

    def __init__(self, name, age, fnd_boot):
        super().__init__(name, age)
        self.fnd_boot = fnd_boot

    def find_cinderella(self, cinderellas: [Cinderella]):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.fnd_boot:
                print(cinderella)
            else:
                print(f'Not a cinderella {cinderella.name}')


cinder_arr: list[Cinderella] = [
    Cinderella('Nika', 20, 30),
    Cinderella('Ira', 21, 29),
    Cinderella('Katya', 22, 32),
    Cinderella('Vika', 23, 33),
]


prince = Prince('Harry', 23, 33)

prince.find_cinderella(cinder_arr)

# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити
# перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

# Приклад:
#
# Main.add(Magazine('Magazine1'))
#     Main.add(Book('Book1'))
#     Main.add(Magazine('Magazine3'))
#     Main.add(Magazine('Magazine2'))
#     Main.add(Book('Book2'))
#
#     Main.show_all_magazines()
#     print('-' * 40)
#     Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False


from abc import ABC, abstractmethod


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book -- [{self.name}]")


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine -- [{self.name}]")


class Main:
    __printable_list: list[Printable] = []

    @classmethod
    def push(cls, item):
        if isinstance(item, (Magazine, Book)):
            cls.__printable_list.append(item)

    @classmethod
    def show_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.push(Book('Harry Potter'))
Main.push(Book('Hobbit'))
Main.push(Book('Sherlock Holmes'))
Main.push(Magazine('Spider-man 1'))
Main.push(Magazine('Spider-man 2'))
Main.push(Magazine('Spider-man 3'))

print('-*-' * 10)
Main.show_magazines()
print('-*-' * 10)
Main.show_books()
print('-*-' * 10)

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# city = input("Enter your city: ")

# print([name, age, city])
# print(name)

# print(dir(name))

# def my_name(name):
#     print(name)

# my_name('Ivan')
# my_list = [1, 22]
# print(my_list)

# a = 10

# def my_fn():
#     print("hello")

# print("ivan")

# def hello(name):
#     res = ("Hello there!", name)
#     return res


# first = hello('Ivan')
# print(first)

# print(hello('World'))

# import datetime

# print(datetime.MAXYEAR)

# my_name = 'Ivan'
# print(id(my_name))

# my_num = 100
# print(id(my_num))
# print(id(my_num))


# info_msg = """You
# are learning the easiest
# programming language -
# Python!"""

# print(info_msg)

# print(type(info_msg))


# my_name = 'Ivan Yakovchuk'

# print(len(my_name))

# print(my_name[:4])

# input_str = input("Enter any number: ")

# input_int = int(input_str)

# print(input_int)

# print(type(input_int))

# base = 5
# power = 3.2
# step_number = pow(base, power)

# print(step_number)
# print(type(step_number))

# step_number = int(step_number)

# print(step_number)
# print(type(step_number))

# long_int = 1_000_000_000

# print(long_int)

# average_price = 28.75
# price = int(average_price)

# print(price)           # 28
# print(type(price))     # <class 'int'>


# str_temperature = '14.5'
# temperature = float(str_temperature)

# print(temperature)        # 14.5
# print(type(temperature))  # <class 'float'>

# my_name = 'Ivan Yakovchuk'
# bool(my_name)
# print(type(my_name))


# db_is_available = False

# print(db_is_available)
# print(type(db_is_available))

# db_is_available = True
# print(db_is_available)

# print(bool(10))
# print(bool('abc'))
# print(bool([]))
# print(bool([1, 2]))
# print(bool(None))

# print(100 > 10)
# print("Long string" > 'Short')
# print([] == [])
# print({'a': 3} == {'a': 3})


# int_num = 50
# float_num = 7.5
# str_val = 'abc'

# print(int_num * str_val)
# print(str_val * int_num)

# print(int_num.__mul__(float_num))
# NotImplemented

# print(float_num.__rmul__(int_num))
# 375.0

# print(str.__doc__)

# my_list = []

# print(help(my_list.__eq__))


# my_fruits = ['apple', 'banana']
# my_fruits2 = ['apple', 'banana']
# # my_fruits2 = ['banana', 'apple']

# print(my_fruits == my_fruits2)


# my_fruits = ['apple', 'banana', 'orange']
# print(len(my_fruits))  # 3 - метод len показує довжину списка

# ratings = [2.5, 5.0, 4.3, 3.7, 4.5]
# print(id(ratings))
# print(id(ratings[:]))
# print(my_name))

# my_nums = [10, 50, 0, 5, 5, 100]

# other_nums = my_nums.copy()

# print(id(my_nums))
# print(id(other_nums))


# ЗАВДАННЯ 1

# my_list = [True, 22, 'abc', None, [5]]

# print(my_list)

# del my_list[2]
# my_list.pop(2)

# # print(my_list)

# print(len(my_list))

# my_list.reverse()

# print(my_list)

# new_my_list = [23, 24]
# print(new_my_list)

# my_list.extend(new_my_list)
# print(my_list)


# ЗАВДАННЯ 2

# my_list = [11, 22, 33, 44]
# new_my_list = [23, 24]


# print(my_list.__add__(new_my_list))


# my_motorbike = {
#     'brand': 'Ducati',
#     'price': '25000',
#     'engine_vol': '1.2',
#     'my_list': [True, 22, 'abc', None, [5]]
# }

# print(my_motorbike)

# my_motorbike = {
#     'brand': 'Ducati',
#     'engine_vol': '1.2',
#     'price': '25000'
# }

# key_name = 'brand'
# my_motorbike[key_name] = 'BMW'
# print(my_motorbike)


# my_dict = {}
# print(my_dict.__doc__)


# my_disk = {}

# print(id(my_disk))
# print(type(my_disk))

# my_disk['price'] = '80'
# my_disk['brand'] = 'Samsung'

# print(my_disk)

# print(id(my_disk))
# print(type(my_disk))

# print(my_disk.items())
# print(type(my_disk.items()))

# print(my_disk.keys())
# print(list(my_disk.keys()))

# print(my_disk.popitem())


# my_list = [['first', 0], ['second', True]]

# my_dict = dict(my_list)

# print(my_dict)

# КОРИСТУВАЧ ВВОДИТЬ ПЕВНІ КЛЮЧІ І ЗНАЧЕННЯ І НА ОСНОВІ ЦЬОГО СТВОРЮЄМО СЛОВНИК

my_dict = {}

keys_one = input("Enter your keys_one: ")
keys_two = input("Enter your keys_two: ")
keys_three = input("Enter your keys_three: ")

value_one = input("Enter your value_one: ")
value_two = input("Enter your value_two: ")
value_three = input("Enter your citvalue_threey: ")

my_dict[keys_one] = value_one
my_dict[keys_two] = value_two
my_dict[keys_three] = value_three

print(my_dict)

# условия
from typing import Callable, Tuple, Any

# простое

name = "Michael"
if name == "Michael":
    print(f"Hello, {name}")

# с иначе
if name == "Michael":
    print(f"Hello, {name}")
else:
    print(f"Name, {name} is not availab")

# с разветвлениями
if name == "Michael":
    print(f"Hello, {name}")
elif name == 'Eugene':
    print(f"Boss, {name}")
else:
    print(f"Name, {name} is not availab")

# арифметический цикл
n = 10
for number in range(10):
    print(number, end=' ')

# цикл с предусловием
while n > 0:
    print(n, end=' ')
    n -= 1

while True:
    print(n)
    if n == 0:
        break
    n += 1

###################################################
# списки
my_list = ["Hello", 100, True]
print(type(my_list))
for value in my_list:
    print(value)

# кортежи
my_tuple = tuple(my_list)
print(type(my_tuple))
for value in my_tuple:
    print(value)

###################################################
# множества
my_set = set(my_list)
print(type(my_set))
for value in my_set:
    print(value)
###################################################
# словари
my_dict = {"1": 100, "2": 200, "3": 400}
print(type(my_dict))
for key, value in my_dict.items():
    print(key, value)


###################################################
# функция без аргументов
def fun_wo_args() -> None:
    print("функция без аргументов")


fun_wo_args()


###################################################
# функция с позиционными аргументами
def fun_with_position_args(arg1: int, arg2: float, arg3: str, square: float = .5) -> str:
    return f"{arg3} : {(arg1 * arg2) ** square}"


print(fun_with_position_args(10, 15.7, "Ответ"))


###################################################
# функция с именованными аргументами
def fun_with_named_args(**kwargs) -> str:
    up = kwargs.get("up")
    low = kwargs.get("low")
    q = kwargs.get("q")
    return f"{q} : {(up * low)}"


print(fun_with_named_args(low=10, up=15.7, q="Ответ"))


###################################################
# функция с произвольными аргументами
def f(*args) -> int:
    return args[2]


print(f(1, 2, 3, 4))


###################################################
# передача функции в качестве аргумента
def simple_word() -> str:
    return "World"


def result(func: Callable) -> str:
    return f"Hello {func()}"


print(result(simple_word))


###################################################
# вложенные функции
def out_func(*args):
    def iner_func(a: int, b: int) -> int:
        return a + b

    return iner_func(args[0], args[1])


print(out_func(1, 2))


###################################################
# обработка ввода данных пользователем
def func_with_user_input(*args) -> tuple[Any, ...]:
    return args


# print(input("Введите слова: "))


###################################################
# создание функции-генератора
def gen_func(number: int):
    for i in range(number, 1, -1):
        yield i


e = 5
i = gen_func(e)
while e > 2:
    e = next(i)
    print(e)

###################################################
# создание выражения-генератора
gen = (n for n in range(10))
print(next(gen))

###################################################
itr = iter([n for n in range(10)])
print(next(itr))


###################################################
# создание декоратора
def decor(func):
    def iner(*args) -> str:
        return f"Сумма {func(args[0], args[1])}"

    return iner


@decor
def sum(a: float, b: float) -> float:
    return a + b


print(sum(1, 2))

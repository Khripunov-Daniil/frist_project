# ________________________________________________Генераторы и ЗАМЫКАНИЯ___________________________________________________

# def func(n):
#     for i in range(n):    #  Генератор 
#         yield i 

# for num in func(5):    # - зацикливаем генератор
#     print(num)



# def power_of_2(n):
#     poww = 1
#     for i in range(n):
#         yield poww
#         poww *= 2

# t = [x for x in power_of_2(5)]  # Генераторы списков 

# t2 = list(power_of_2(5))  # Преобразования в список
# print(t)
# print(t2)


# __________________________________________________Лямда функция________________________________________________

# lambda  параметры: выражение 

# two = lambda: 2
# square = lambda x: x ** 2
# pwr = lambda x, y: x ** y

# for i in range (-2, 3):
#     print(square(i), end=" ")
#     print(pwr(i, two()))

# def printfunction(args, func):
#     for x in args:
#         print(f"f({func(x)})")


# # def poly(x):
# #     return 2 * x ** 2 - 4 * x + 2

# printfunction([x for x in range(-2,3)], lambda x: 2 * x ** 2 - 4 * x + 2 )

#  map(function, list)

# list1 = [x for x in range (5)]

# list2 = list(map(lambda x: x ** 2, list1 ))
# print(list2)

# for x in map(lambda x : x ** 2 , list2):
#     print(x, end=" ")
# print()

# list1 = [i for i in range(51)]
# list2 = sum(list(map(lambda x: x, list1)))

# print(list2)


# list1 = [i for i in range(51)]
# total = 0
# for x in (map(lambda x: x, list1)):
#     total += x 
# print(total)


# from random import  randint


# data = [randint(-10,10) for x in range(5)]
# filtered = list(filter(lambda x : x > 0 and x % 2 == 0 , data))
# print(data)
# print(filtered)


# names = [ "ваня ", "вася", "петя ", "катя", "Даниил ", "Алексей ", "Ольга ", "Светлана", "Сурен", "Ослан"]
# filtered = list(filter(lambda x : x.istitle(), names))
# print(filtered)

# arr = [1,2,3,4,"5",6,"7",8,"9",10]

# filtered = list(filter(lambda x : x == int(x), arr))
# print(filtered)

# filtered2 = list(map(lambda x :  str(x) if type(x) == int else x, arr))
# print(filtered2)

# filtered3 = list(map(lambda x :  int(x) if type(x) == str else x, arr))
# print(filtered3)

# arr1 = [1,2,3,4]
# arr2 = ["one","two","three","foor"]
# new_arr = list(map(lambda a, b: (a,b), arr1, arr2 ))
# print(new_arr)


# from functools import reduce

# # reduse(func, list, [initial]) - уменьшает массив до 1 значения


# list1 = [i for i in range(10)]

# total = reduce(lambda x, y: x*y, list1)
# print(total)


words = ["qwerty", "python", "acbca", "мадам", "казак"]

filtered = list(filter(lambda x : x == x[::-1], words))
print(filtered)
filtered2 = list(filter(lambda x : x != x[::-1], words))
print(filtered2)

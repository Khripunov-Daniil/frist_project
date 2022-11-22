# __________________________________КОРТЕЖИ МНОЖЕСТВА СЛОВАРИ__________________________________________

# obj = {}
# obj2 = dict()
# print(type(obj))
# print(type(obj2))

# obj = {}

# obj["name"] = "ИВАН"

# print(obj)

# capitals = {}
# capitals["Russia"] = " Moscou"
# capitals["Belarus"] = "Minsk"
# capitals["Kazahstan"] = "Astana"

# countries = ["Russia","Belarus", "Kazahstan"]
# for country in capitals:
#     print(f"Столица страны {country}: {capitals[country]}")

# print(capitals.get("Turkmenistan"))   # Вызывает ошибку KeyError
# print(capitals["Turkmenistan"])          # Возврощает None

# QueryDict - название JSON  в Python
# # Вщзвращает пары поочередно
# for obj in capitals.items():
#     print(obj)
# # Вщзвращает ключи поочередно
# for cantry in capitals.keys():
#     print(cantry)
#     # Вщзвращает значение поочередно
# for capytal in capitals.values():
#     print(capytal) 



# capitals = {}
# capitals["Russia"] = " Moscou"
# capitals["Belarus"] = "Minsk"
# capitals["Kazahstan"] = "Astana"

# for coutnry, item in capitals.items():
#     print(f"Столица страны {coutnry} - {item}")

#  .pop(key) -  удаляет ключ и значение
#  
# capitals.pop("Kazahstan")
# print(capitals)

#  .popitem -  удаляет последнюю пару и значение

# capitals.popitem()
# print(capitals)


#  ubdate = обновляет словарь добавляет из второго словаря в первый

# dict1 = {"one": "один", "two": "Два"}
# dict2 = {"Three": "три", "four": "четыре"}

# dict1.update(dict2)
# print(dict1)

# __________________________________________________________________________________________
# obj = {}
# obj2 = dict()
# print(type(obj))
# print(type(obj2))

# capitals = {}
# capitals["Russia"] = " Moscou"
# capitals["Belarus"] = "Minsk"
# capitals["Kazahstan"] = "Astana"

# # Вщзвращает пары поочередно
# for obj in capitals.items():
#     print(obj)
# # Вщзвращает ключи поочередно
# for cantry in capitals.keys():
#     print(cantry)
#     # Вщзвращает значение поочередно
# for capytal in capitals.values():
#     print(capytal) 
#  .pop(key) -  удаляет ключ и значение
# #  .popitem -  удаляет последнюю пару и значение
# ubdate = обновляет словарь добавляет из второго словаря в первый 
# _______________________________________________________________________________________________

# str_dict = {x:y for x in "abc" for y in "xyz"}
# print(str_dict)

# dict3 = {x: x**2 for x in range(1,5)}
# print(dict3)


# arr1 = ["Зима", "Весна","Лето", "Осень"]
# arr2 = [[1,2,12], [3,4,5],[6,7,8],[9,10,11]]
# season_with_months= {}
# for i in range (0, len(arr1)):
#     season_with_months[arr1[i]] = arr2[i]
# print(season_with_months)



# arr1 = ["Зима", "Весна","Лето", "Осень"]
# arr2 = [[1,2,12], [3,4,5],[6,7,8],[9,10,11]]
# season_with_months= {}

# season_with_months = dict(zip(arr1,arr2))
# print(season_with_months)
# ______________________________________1______________________
# from itertools import count


# dict1 = {"one": "один", "two": "Два"}
# dict2 = {"Three": "три", "four": "четыре"}

# dict1.update(dict2)
# print(dict1)
# # __________________________________________2______________________

# num_arr = {"one": 1,"two": 2,"three": 3,"four": 4,"five": 5,}
# total = 1
# for num in num_arr.values():    # - значе
#     total *= num
# print(total)


# ______________________________________________3______________________
# import re
# str = "Пайтон  один из самых популярных языков програмирования"

# str = re.sub(r'\s+', '', str)
# str = str.lower()
# for i in str:
#     x = str.count(i)
    
#     print(f"{i} количество вхождений {x}")


# str = "Пайтон  один из самых популярных языков програмирования"
# str_obj = {}
# for i in range(len(str)):
#     str_obj[str[i]] = f"количество вхождений - {str.count(str[i])} " 

# print(str_obj)


# ________________________________________________________________МНОЖЕСТВА___________________________________________
# хранит в себе только уникальные элементы
# a = set()
# print(type(a))

# string = set("hello world")
# print(string)

# string.add("p")   # -  добавляет элемент в нашем случае р
# print(string)

# string.remove("p")   #  вызывает keyarror  если такого элемента нет
# string.discard("p")  #  удаляет элемент если он есть в множестве
# string.pop() #  удаляет первый элемент в множестве


# ________________________________________________________________КОРТЕЖИ___________________________________________
# не изменяемый тип данных

# cake = ("c", "a", "k", "e")
# print(type(cake))

# print(cake[2:4])


# a = (1,2,3,4)
# b = (5,6,7,8)
# c = a *2
# print(c)

arr =[
    {"name": "Alex",  "is_active": True},
    {"name": "John" ,"is_active": False},
    {"name": "Sam", "is_active": True},
    {"name": "Dilon", "is_active": False},
]

for i in arr:
    if i.keys("is_active") ==  True:
        print(f"{i.values()} account is active")
    else:
        print(f"{i.values()} account is not active")

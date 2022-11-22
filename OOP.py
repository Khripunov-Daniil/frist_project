# ________________________________ООП______Объектно ориентированное программирование______________________________
# класс = чертёж
# класс = экземпляр - продукт созданный при помощи чертежа

# class Cat():
#     def __init__(self, name, age, color, breed):    # self -  обязательный элемент      __init__ - имеет свойство и помогает инициализировать для создания перечня свойств
#         self.name = name
#         self.age = age
#         self.color = color
#         self.breed = breed
    
#     # метод доступный только внутри этого класса
#     def say_hello(self):
#         return f"Мяу, меня зовут {self.name}"

# cat = Cat("Барсик", 3, "черно-белый", "дворняга")
# cat2 = Cat(color = "черно-белый", breed = "дворняга", name = "Барсик", age = 3)
# print(cat.name)
# print(cat.age)
# print(cat.color)
# print(cat.breed)
# print(cat.say_hello())


# ______________________________________________________________три термина на которых держится ООП

# ____________________________________________________________________1 - Наследование 
# ____________________________________________________________________2- инкапсуляция
# ____________________________________________________________________3 - полиморфизм


class Animal:                                 #Супер класс Animal
    def __init__(self, age, breed, life_time ):
        self.age = age
        self.breed = breed
        self.life_time = life_time
    
    def animal_intro(self):
        return f"Привет моя порода {self.breed}"
    
class Pet(Animal):                             # подкласс животное  Pet(Animal)
    def __init__(self, weight, height, name, age, breed):
        super().__init__(age, breed)            # обращение к родительскому классу Super для наследования и добавки доп. метода
        self.name = name                         # добавкa доп. метода
        self.weight = weight
        self.height = height
    
    def pet_intro(self):                      #  для того чтобы переписать тело  заменитьб добавить значение
        super().animal_intro()
        return f"Я  {self.name}"
    
        

class Wild(Animal):
    def __init__(self, age, breed, animal_type):
        super().__init__(age,breed)
        self.animal_type = animal_type
    
    def introduce(self):
        return f"Моя порода  {self.breed}  из  {self.animal_type}"

class Cat(Animal):

    def __init__(self,length_of_wool, age, breed, animal_type, life_time):
        super().__init__(length_of_wool)
        self.length_of_wool = length_of_wool
        return f" Хочу гулять"
    def introduced(self):
        return f" ,бегаю по дому"


# dog = Pet(name = 'Шарик', age = 3, breed = "Терьер", weight = " 10 кг", height = " 20 см" )
# print(dog.age)
# print(dog.breed)
# print(dog.name)
# print(dog.animal_intro())
# print(dog.pet_intro())

# leo = Wild(animal_type = "Кошачьего семейства", age = 5, breed = "Африканская")
cat = Cat(name = "мурзик", age = 5, length_of_wool= "10 cm", breed = "Cиамскиая", weight = " 10 кг", height = " 20 см", life_time = "10 лет")

# print(leo.animal_type)
# print(leo.animal_intro())
# print(leo.introduce())
print(cat.length_of_wool)

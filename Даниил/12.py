
import random


num = [random.randint(1,10000) for i in range(10)]
print(num)

def func(num):
    num.sort()

    num2 = num[1] + num[0]
    return num2
print(func(num))
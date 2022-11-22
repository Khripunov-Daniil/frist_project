import random


num = [random.randint(1,10) for i in range(10)]

print(num)

def number(num):
    sorted(num)
    return list(reversed(num))

print(number(num))



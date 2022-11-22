import random

num1 = random.randint(1,10)

num2 = random.randint(1,10)

def arr(num1, num2):
    if num1 == num2:
        return f"Площадь {num1**2}"
    elif num1 != num2:
        return f"Периметр  {(num1 +num2)*2}"

print(arr(num1, num2))


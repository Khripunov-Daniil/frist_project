
import random

y = random.randint(1,10)
n = random.randint(10, 20)
x = random.randint(1,10)

def number(n, x, y):
    if n % x == 0 or n % y == 0:
        return True
    else:
        return False
    
print(number(n, x, y))



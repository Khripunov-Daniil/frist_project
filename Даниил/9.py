
import random

cap = random.randint(1,40)
on = random.randint(1, 40)
x = random.randint(1,40)
num = 0 
def buss(cap, on, x):
    num = cap - on 
    if num >= x :
        return num
    else: 
        return 0 

print(buss(cap, on, x))
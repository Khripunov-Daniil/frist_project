import random

timmi = random.randint(1,5)

sara = random.randint(1,5)

def love(timmi, sara):
    if timmi == sara:
        return True
    else:
        return False


print(love(timmi,sara))
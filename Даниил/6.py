import random

def bmi(wes,rost):
    rost = rost / 100
    imt = wes / rost **2
    print(imt)
    if imt <= 18.5:
        return "Недостаточный вес "
    if 18.5 <= imt <= 25.0:
        return "Нормально "
    if 25.0 <= imt <= 30.0:
        return "Избыточный вес"
    if imt > 30:
        return "Ожирение "
    else:
        return "Arror"

print(bmi(70, 170))




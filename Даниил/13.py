
arr = ["Телескопы", "Глаза","очки", "Монокли"]

def func(arr):
    arr = sorted(arr, key=len)
    return arr
               

print(func(arr))



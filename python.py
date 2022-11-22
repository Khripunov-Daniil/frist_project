# ____________________________________СОРТИРОВКА____________________________________



# ______________________МЕТОД ПУЗЫРЬКА:______________________________
# n = 10
# a = [] 
# for i in range (n):
#     a.append(randint(1,99))
# print(a)

# for i in range (n -1):
#     for j in range(n-i-1):
#         if a[j] < a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# print(a)


# i = 0 
# while i < n - 1:
#     j = 0 
#     while j < n - 1  - i:
#         if a[j] < a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
#         j +=1
#     i+=1
# print (a)

# _____________________________________СОРТИРОВКА СЛИЯНИЕМ________________________________________________
# from random import randint

# def merg_sort(alist, start, end):
#     if end - start > 1 :
#         mid = (start + end) // 2
#         print(mid)
#         merg_sort(alist, start, mid)
#         print(alist, start, mid)
#         merg_sort(alist, mid, end)
#         print(alist, mid, end)
#         merg_list(alist, start, mid , end)
#         print(alist, start, mid , end)
        

# def merg_list(alist, start, mid, end):
#     left = alist[start : mid]
#     right = alist[mid: end]
#     k = start
#     i = 0
#     j = 0
#     while (start + i  < mid and mid + j < end):
#         if left [i] <= right[j]:
#             alist[k] = left[i]
#             i += 1
#         else:
#             alist[k] = right[j]
#             j += 1
#         k += 1
#     if start + i < mid:
#         while k < end:
#             alist[k] = left[i]
#             i += 1
#             k += 1
#     else:
#         while k < end:
#             alist[k] = right[j]
#             j += 1
#             k += 1
# alist = [randint(1,99) for i in range (10)]
# merg_sort(alist, 0, len(alist))
# print(alist)
# print("sorted", alist)


# __________________________________СОРТИРОВКА ВСТАВКАМИ_________________________________________________
# from random import randint

# def insertion_sort(array):
#     for i in range (1, len(array)):

#         key = array[i]
#         j = i - 1
#         while array[j] > key and j >= 0:
#             array[j+1] = array[j]
#             j -= 1
#         array[j+1] = key
#     return array

# lst = [randint(1,99) for i in range (10)]
# print(lst)
# print(insertion_sort(lst))

# __________________________________СОРТИРОВКА ШЕЛЛА_________________________________________________

from random import randint
import math


def shell_sort (arr):
    n = len(arr)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0 :
        for i in range(interval, n):
            temp = arr[i]
            j = i 
            while j >= interval and arr[j - interval] > temp:
                arr[j] = arr[j - interval]
                j -= interval
            arr[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return arr
lst = [randint(1,99) for r in range (10)]
print(lst)
shell_sort(lst)
print(lst)
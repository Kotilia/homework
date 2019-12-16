#Кот Илья Аи-182
from random import randrange
import time
from datetime import datetime
import random

#buble
my_list = [ randrange(0, 15) for i in range(10) ]
#Сортировка слиянием
def merge_sort(mass):
    lenght = len(mass)
    if lenght >= 2:
        mid = int(lenght / 2)
        mass = merge(merge_sort(mass[:mid]), merge_sort(mass[mid:]))
        return mass;
def merge(mass1, mass2): 
    res = [] 
    while mass1 and mass2: 
        if mass1[0] < mass2[0]: 
            res.append(mass1.pop(0)) 
        else: res.append(mass2.pop(0)) 
    if mass1: 
        res.extend(mass1) 
    if mass2: 
        res.extend(mass2) 
    return res

max_list = len( my_list )

i = 0
while i < max_list:

    j = 0
    while j < max_list-i-1:
#Сортировка кучей
def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

        if my_list[ j ] > my_list[ j + 1 ]:
def heap_sort(nums):  
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

            my_list[ j ], my_list[ j + 1] = my_list[ j + 1], my_list[ j ]
        j+=1
    i += 1

print( my_list )
#Быстрая Сортировка
def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem) 
            elif elem > q: 
                R.append(elem) 
            else: 
                M.append(elem)
        return QuickSort(L) + M + QuickSort(R)

mass = '72940610672875';
array = []
i = 0
lenght = len(mass)

while i < lenght:
    array.append(int(mass[i]))
    i += 1

from datetime import datetime
print(array) 
start_time = datetime.now()
# do your work here
print(QuickSort(array))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time)) 
print('Duration: {}'.format(end_time - start_time))
array = []
i = 0
lenght = len(mass)

while i < lenght:
    array.append(int(mass[i]))
    i += 1
print(heap_sort(array))

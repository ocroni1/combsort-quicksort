import random
import time
def comb_sort(array): # сортировка расчёской
    n = len(array)
    gap = n
    swapped = True
    factor = 1.247 # фактор уменьшения
    while (gap>1) or swapped:
        if gap>1:
            gap = int(gap/factor) # уменьшается шаг
        if gap < 1:
            gap = 1
        swapped = False
        i = 0
        while i+gap<n:
            if array[i]>array[i+gap]:
                array[i], array[i+gap] = array[i+gap], array[i] # сравниваются элементы, отстоящие друг от друга на gap
                swapped = True # если был обмен – ещё один проход нужен
            i+=1
    return array

def quicksort(array): # быстрая сортировка
    n = len(array)
    if n < 2:
        return array
    rand = random.randint(0, n-1)
    pivot = array[rand]
    left = []
    right = []
    middle = []
    for i in range(n):
        # тройное разбиение массива относительно опорного элемента
        if (array[i]<pivot):
            left.append(array[i])
        elif (array[i]>pivot):
            right.append(array[i])
        else:
            middle.append(array[i])
    return quicksort(left)+middle+quicksort(right)

narr = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 100000]
for n in narr: # Перебор количества элементов для теста
    timequick = 0 # Среднее время работы quicksort
    timecomb = 0 # Среднее время работы comb sort
    for i in range (10000): # 10000 тестовых массивов
        randarr = [random.randint(-100000, 100000) for _ in range(n)] # случайный массив
        # Тестируем comb sort на копии исходного массива
        arr_comb = randarr.copy()
        startcomb = time.perf_counter() #Начало отсчёта для comb sort
        comb_sort(arr_comb)
        timecomb += time.perf_counter() - startcomb

        # Тестируем quicksort на копии исходного массива
        arr_quick = randarr.copy()
        startquick = time.perf_counter()  # Начало отсчёта для quicksort
        quicksort(arr_quick)
        timequick += time.perf_counter() - startquick
    timecomb /= 10000 #Усредняем время
    timequick /= 10000
    print(f'Среднее время для {n} элементов:\ncomb sort:', timecomb, "\nquicksort:", timequick)

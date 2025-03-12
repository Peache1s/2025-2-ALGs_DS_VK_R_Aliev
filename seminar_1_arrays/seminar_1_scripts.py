"""
Модуль со скриптами с 1-ого семинара
"""


def two_sum(nums, target):
    """
    Ищет в отсортированном по возрастанию массиве целых чисел nums элементы,
    в сумме дающие target, возвращает их индексы

    :param nums: отсортированный по возрастанию массив целых чисел
    :param target: искомая сумма двух элементов
    :return: индексы двух элементов в массиве с суммой равной target
    """
    left = 0
    right = len(nums) - 1

    while left < right:
        summ = nums[left] + nums[right]

        if summ == target:
            return [left, right]
        elif summ < target:
            left += 1
        else:
            right -= 1
    return []


def reverse_array(arr, left=-1, right=-1):
    """
    Разворачивает массив целых чисел или его внутреннюю часть arr[left:right]

    :param arr: массив целых чисел
    :param left: левый индекс подмассива
    :param right: правый индекс подмассива
    :return:
    """
    if left == -1 and right == -1:
        left = 0
        right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def reverse_array_part(arr, k):
    """
    Сдвигает справа налево часть массива arr размером k

    :param arr: массив целых чисел
    :param k: число элементов справа для поворота
    :return: перевернутый массив
    """
    n = len(arr)
    print(arr)
    reverse_array(arr, 0, n - 1)
    reverse_array(arr, 0, k % n - 1)
    reverse_array(arr, k % n, n - 1)

    return arr


def merge_sorted_arrays_with_alloc(arr1, arr2):
    """
    Слияние двух отсортированных массивов с дополнительной аллокацией памяти

    :param arr1: 1-ый отсортированный массив
    :param arr2: 2-ый отсортированный массив
    :return: объединенный отсортированный массив
    """
    merged_array = []

    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    merged_array.extend(arr1[i:])  # == append len(arr1[i:]) раз или можно изначально задать размер и по индексам
    merged_array.extend(arr2[j:])

    return merged_array


def merge_sorted_arrays_without_alloc(arr1, arr2):
    """
    Слияние двух отсортированных массивов без дополнительной аллокацией памяти

    :param arr1: 1-ый отсортированный массив
    :param arr2: 2-ый отсортированный массив
    :return: объединенный отсортированный массив
    """

    p1 = len(arr1) - len(arr2) - 1
    p2 = len(arr2) - 1
    p3 = len(arr1) - 1

    while p2 >= 0:
        if p1 >= 0 and arr1[p1] > arr2[p2]:
            arr1[p3] = arr1[p1]
            p1 -= 1
        else:
            arr1[p3] = arr2[p2]
            p2 -= 1
        p3 -= 1

    return arr1


def sort_binary_array(arr):
    """
    Сортировка массива arr, состоящего 0 и 1

    :param arr: массив из 0 и 1
    :return: отсортированный массив
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


def sort_colors(arr):
    """
    Сортировка массива arr, состоящего из 0, 1 и 2

    :param arr: массив из 0, 1, 2
    :return: отсортированный массив
    """

    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


def even_first(arr):
    """
    Переносит в начало массива все четные числа, сохраняя их очередность

    :param arr: неотсортированный массив целых чисел
    :return: массив с четными числами в начале
    """
    even_index = 0

    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1

    return arr


def zeros_last(arr):
    """
    Переносит в конец массива целых чисел все содержающиеся нули,
    сохраняя очередность ненулевых значений

    :param arr: массив целых чисел
    :return: массив целых чисел с 0 в конце
    """
    not_zero_index = 0

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[not_zero_index] = arr[not_zero_index], arr[i]
            not_zero_index += 1

    return arr

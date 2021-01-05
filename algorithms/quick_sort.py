
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    stand = arr[0]
    left = list(filter(lambda x: x < stand, arr))
    center = list(filter(lambda x: x == stand, arr))
    right = list(filter(lambda x: x > stand, arr))

    return quick_sort(left) + center + quick_sort(right)


l = [6, 2, 4, 1, 9, 9, 6, 7, 6]
print(quick_sort(l))

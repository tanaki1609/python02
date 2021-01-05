# Quick sort - recursively
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    elem = arr[0]
    left = [i for i in arr if i < elem]
    center = list(filter(lambda x: x == elem, arr))
    right = []
    for j in arr:
        if j > elem:
            right.append(j)
    print('left: ', left)
    print('center: ', center)
    print('right: ', right)
    print()
    return quick_sort(left) + center + quick_sort(right)


arr = [50, 34, 77, 89, 25, 12, 50, 88, 100, 99, 22, 11, 64]
print(quick_sort(arr))

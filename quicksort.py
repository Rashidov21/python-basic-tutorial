# def countdown(i):
#     if i <= 0:
#         return None
#     print(i)
#     return countdown(i - 1)
#
#
# countdown(10)


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([1,8,3,6,4,5,7,9,2]))
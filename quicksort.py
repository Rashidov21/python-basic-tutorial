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

# for i in range(len("alpha")*2,2*8):
#     print(i)
# print(*[x for x in [0,2,-1,-6,5] if x > 0])
print(sum([x for x in range(-3, 6)]))
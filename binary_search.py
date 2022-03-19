def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    steps = 0
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return f"Steps = {steps} : Item = {mid}"
        if guess > item:
            high = mid - 1
            print("Kichik")
        else:
            low = mid + 1
            print("Katta")
        steps += 1
    return None

l = list(range(24000*10))
print(binary_search(l, 1000))

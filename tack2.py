def fibonacci_generator(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1
    return fibonacci_generator(n - 1) + fibonacci_generator(n - 2)


def fibonacci_search(arr, x):
    m = 0
    while fibonacci_generator(m) < len(arr):
        m = m + 1
    offset = -1
    while fibonacci_generator(m) > 1:
        i = min(offset + fibonacci_generator(m - 2), len(arr) - 1)
        if x > arr[i]:
            m = m - 1
            offset = i
        elif x < arr[i]:
            m = m - 2
        else:
            return i
    if fibonacci_generator(m - 1) and arr[offset + 1] == x:
        return offset + 1
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8]
print('Number found at index : ', fibonacci_search(arr, 8))

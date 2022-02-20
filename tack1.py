def binary_search(arr, left_board, right_board, x):

    if right_board >= left_board:
        mid = left_board + (right_board - left_board) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, left_board, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, right_board, x)
    else:
        return


arr = [2, 3, 4, 10, 40]
x = 10
y = 1
print(binary_search(arr, 0, len(arr) - 1, x))
print(binary_search(arr, 0, len(arr) - 1, y))

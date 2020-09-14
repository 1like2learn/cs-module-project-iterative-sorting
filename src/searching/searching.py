def linear_search(arr, target):
    # Your code here
    for item in arr:
        if item == target:
            return arr.index(target)

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # Dimension variables for the top and bottom indexes
    bot = 0
    top = len(arr) - 1
    # Loop while the bot i
    while bot <= top:
        mid = (bot + top) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            top = mid -1
        else:
            bot = mid + 1

    return -1  # not found

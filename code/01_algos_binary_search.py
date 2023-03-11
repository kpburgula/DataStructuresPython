### Binary Search
## Array of elements need to be sorted
## Worst case time complexity is O(log(n))


def binary_search(n, x):
    low = 0
    high = len(n) - 1
    mid = (low + high) // 2
    while low <= high:
        print(low, mid, high)
        if n[mid] == x:
            print("Found Element at index: ", mid)
            return mid
        elif n[mid] > x:
            high = mid - 1
            mid = (low + high) // 2
        elif n[mid] < x:
            low = mid + 1
            mid = (low + high) // 2
    print('Element not found')
    return -1


# Array of integers
n = [1, 12, 23, 44, 55, 62, 70]
x = 62
binary_search(n, x)
# Array of strings
# n = ["boat", "cow", "pradeep", "quail", "yacht", "Zeb", "zoo"]
# binary_search(n, "Zeb")

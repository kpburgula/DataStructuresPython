# divide and conquer algorithm
# Step 1: Create a base case
# Step 2: Break the problem until it reaches base case


def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


print(sum(list(range(100))))


def count(arr):
    if arr == []:
        return 0
    else:
        return 1 + count(arr[1:])


print(count(list(range(100))))


def max_num(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[0] if arr[1] < arr[0] else arr[1]
    temp = max(arr[1:])
    return arr[0] if arr[0] > temp else temp


print(max_num([5, 3, 7]))


def binary_search(arr, x, low, high, mid):

    if (len(arr) == 1 & arr[0] == x):  #base case
        return mid
    elif arr[mid] > x:
        return binary_search(n[low:mid - 1], x, low, mid - 1,
                             (low + mid - 1) // 2)
    elif arr[mid] < x:
        return binary_search(n[mid + 1:high], x, mid + 1, high,
                             (mid + 1 + high) // 2)


n = [1, 2, 3, 4]
val = 3
l = 0
h = len(n) - 1
m = (l + h) // 2

print(binary_search(n, val, l, h, m))

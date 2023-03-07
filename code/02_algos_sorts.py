# Selection sort is the basic sort with a time complexity of O(n**2)


def selection_sort(n):
    def find_smallest(temp):
        small = temp[0]
        index = 0
        for i in range(len(temp)):
            if temp[i] < small:
                small = temp[i]
                index = i

        return small, index

    sorted = []
    for i in range(len(n)):
        val, ix = find_smallest(n)
        # print(val, ix)
        sorted.append(val)
        n.pop(ix)
    return sorted


# Array of integers
print(selection_sort([43, 57, 3, 2, 6, 45, 876, 453, 24, 1, -2, -4]))

# Array of Strings
print(
    selection_sort(['kp', 'burgula', 'apple', 'butterscotch', 'zoo', 'yacht']))

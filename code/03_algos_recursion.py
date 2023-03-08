# two cases:
# base case: when the function doesn't call itself
# recursive case: when the function calls itself again


# A simple recursive function
def recursive_func(num):
    if num <= 0:
        return
    else:
        print(num)
        recursive_func(num - 1)


recursive_func(10)

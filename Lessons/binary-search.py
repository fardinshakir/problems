def my_function(x, array):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low + high) // 2

        if array[mid] > x:
            high = mid - 1
        elif array[mid] < x:
            low = mid + 1
        else:
            return mid
    return -1
if __name__ == "__main__":
    x = 5
    array = list(range(1, 11))
    result = my_function(x, array)
    print(x, array[result])

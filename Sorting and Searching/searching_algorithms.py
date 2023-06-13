def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i

    return  -1

def binary_search(array, value):

    middle = len(array) // 2

    if len(array) == 0:
        return False

    elif array[middle] == value:
        return True
    elif array[middle] > value:
        return binary_search(array[:middle], value)
    else:
        return binary_search(array[middle+1:], value)

def binary_search_index(array, value):
    start = 0
    end = len(array) -1
    middle = (start + end) // 2

    while True:
        if array[middle] == value:
            return middle
        elif start > end:
            return -1

        if array[middle] < value:
            start = middle + 1
        else:
            end = middle - 1

        middle = (start + end) // 2

def binary_search_index_2(array, value, start=0, end=None):
    if end is None:
        end = len(array) -1

    if start > end:
        return -1

    mid = (start + end ) // 2

    if array[mid] == value:
        return mid
    if array[mid] < value:
        return binary_search_index_2(array, value, mid +1, end)
    else:
        return  binary_search_index_2(array, value, start, mid -1)





array = [1,2,3,4,5,9,8,7,6,5]
print(linear_search(array,100))
array = [10,20,70,88,193]
print(binary_search(array, 3))
print(binary_search_index(array, -90))
print(binary_search_index_2(array, -71))

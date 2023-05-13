def search(array, val):
    begin = 0
    end = len(array)-1
    index = None
    while begin <= end:
        mid = int((begin+end)/2)

        if val == array[mid]:
            index = mid
            end = mid-1

        elif val > array[mid]:
            begin = mid+1

        elif val < array[mid]:
            end = mid-1
    return begin


array = [100, 2, 10, 50, 20, 500, 100, 150, 200, 1000, 100]

array = sorted(array)
print(array)

key = int(30)
lowerbound = search(array, key)
array.insert(lowerbound, key)
print("new array", array)

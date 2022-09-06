def move_zeros(arr):
    length = len(arr)
    for i in range(length):
        if(arr[i] == 0):
            arr.pop(i)
            arr.append(0)
    return arr
    
def missing_number(arr):
    count = 1
    for i in range(len(arr)):
        if (count not in arr):
            return count
        count += 1
    return None

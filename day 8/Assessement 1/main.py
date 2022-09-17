def bool_arr(arr):
    ret_arr=[]
    for n in arr:
        if n%2==0:
            ret_arr.append(True)
        else:
            ret_arr.append(False)
    return ret_arr
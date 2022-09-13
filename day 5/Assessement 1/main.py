from functools import reduce

def get_the_array():
    size = int(input("Enter the amount of numbers in array: "))
    arr = []
    while(size):
        arr.append(int(input("Enter the number: ")))
        size-=1
    return arr

def adj_el():
    numbers = get_the_array()
    max = 0
    if(len(numbers) == 1 ):
        return numbers[0]
    elif(len(numbers) == 0 ):
        return 0
    for i in range(len(numbers)-1):
        if(max<numbers[i]*numbers[i+1]):
            max = numbers[i]*numbers[i+1]
    return max

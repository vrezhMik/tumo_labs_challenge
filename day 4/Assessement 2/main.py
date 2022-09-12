# from statistics import mean 
def list_avg():
    list_l = int(input("Enter the amount of numbers: "))
    numbers = []
    sum = 0;
    while(list_l):
        numbers.append(int(input("Enter a num: ")))
        list_l-=1
    # return mean(numbers)
    for i in numbers:
        sum += i
    return int(sum/len(numbers))
        
print(list_avg())
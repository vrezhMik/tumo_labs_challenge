def sum_of_numbers():
    num = int(input("Enter the num: "))
    sum = 0
    while(num):
        sum += num%10
        num = int(num /10)
    return sum

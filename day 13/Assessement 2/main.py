def fib():
    count = int(input("Enter the length: "))
    first = 0
    second = 1
    print(first)
    print(second)
    l = 2
    while l < count:
        n = first + second
        print(n)
        first = second
        second = n
        l+=1
fib()
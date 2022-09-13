sortedArr = sorted(arr,reverse=True)    
    highest = sortedArr[0]
    secondHighest = 0
    for x in (sortedArr):
        if(x == highest):
            continue
        else:
            secondHighest = x
            break
    print(secondHighest)
def missing_card(N,cards):
    i = N-1
    while(i):
        if i not in cards:
            return i
        i-=1
    return None
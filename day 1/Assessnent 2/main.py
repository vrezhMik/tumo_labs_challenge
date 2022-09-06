def substr(s):
    last = {}
    length = 0
    start = 0
 
    for i in range(0, len(s)):
        if s[i] in last:
            start = max(start, last[s[i]] + 1)
        length = max(length, i-start + 1)
        last[s[i]] = i
    return length
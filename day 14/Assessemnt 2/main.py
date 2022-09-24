def queen(x,y, xd, yd):
    if y == yd or x == xd or abs(y - yd) == abs(x - xd):
        return ("YES")
    else:
        return ("NO")
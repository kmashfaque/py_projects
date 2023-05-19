def mysqrtx(x):
    high = x
    low = 0
    mid = None
    while high-low > .0000000001:
        mid = ((high+low)/2)

        if mid*mid < x:
            low = mid

        else:
            high = mid

    return mid


print(mysqrtx(15))

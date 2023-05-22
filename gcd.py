def gcd(n, m):
    while m % n != 0:
        old_n = n
        old_m = m

        m = old_n
        n = old_m % old_n

    return n


print(gcd(30, 88))

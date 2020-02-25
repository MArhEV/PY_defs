def r_factorial(n):
    if n == 0:
        return 1
    else:
        return n*r_factorial(n-1)
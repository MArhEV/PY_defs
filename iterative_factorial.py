def i_factorial(n):
    result = 1
    if n == 0:
        return 1
    else:
        for each in range(1,n+1):
            result = result*each
        return result
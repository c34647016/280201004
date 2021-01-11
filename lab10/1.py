def multiply3(n):
    if n == 0:
        return 0
    else:
        return multiply3(n - 1) + 3



print(multiply3(6))
def near_hundred(n):
    """
    Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
    """
    return abs(n - 100) < 11 or abs(n - 200) < 11


print(near_hundred(93))
print(near_hundred(90))
print(near_hundred(89))

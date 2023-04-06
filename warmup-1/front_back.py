def front_back(str):
    """
    Given a string, return a new string where the first and last chars
    have been exchanged.
    """
    if len(str) < 2:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


print(front_back("code"))
print(front_back("a"))
print(front_back("ab"))

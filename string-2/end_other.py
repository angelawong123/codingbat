def end_other(a, b):
    """
    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
    """
    a = a.lower()
    b = b.lower()
    if len(a) < len(b):
        a, b = b, a
    return a[-len(b):] == b

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
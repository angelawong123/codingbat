def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat_num = str.count('cat')
    dog_num = str.count('dog')
    if cat_num == dog_num:
        return True
    else:
        return False
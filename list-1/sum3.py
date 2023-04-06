def sum3(nums):
    """
    Given an array of ints length 3, return the sum of all the elements.
    """
    sum = 0
    for numbers in nums:
        sum += numbers
    return sum

print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))
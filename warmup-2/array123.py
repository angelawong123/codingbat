def array123(nums):
    """
    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
    """  
    for i in range(0,len(nums)-2):
        if [1,2,3] == nums[i:i+3]:
            return True
    return False
    
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))
    

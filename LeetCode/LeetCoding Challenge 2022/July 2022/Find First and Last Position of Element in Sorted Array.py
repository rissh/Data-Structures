
def first(nums, x, n):
    
    low = 0
    high = n - 1
    res = -1
    
    while (low <= high):
        mid = (low + high) // 2
        
        if nums[mid] > x:
            high = mid - 1
        elif nums[mid] < x:
            low = mid + 1
        else:
            res = mid
            high = mid - 1

    return res
def last(nums,x, n):
    
    low = 0
    high = n - 1
    res = -1
    
    while(low <= high):
        mid = (low + high) // 2
        
        if nums[mid] > x:
            high = mid - 1
        elif nums[mid] < x:
            low = mid + 1 
        else:
            res = mid
            low = mid + 1

    return res

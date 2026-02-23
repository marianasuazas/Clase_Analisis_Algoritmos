def containsDuplicate(nums):
    
    nums.sort()  
    tamaño = len(nums)
    i = 0
    while i < tamaño - 1:
            
        if nums[i] == nums[i+1] :
            return True
            
        i += 1
            
        
    return False


def containsDuplicate(nums):
    tamaño = len(nums)
    
    i = 0
    while i < tamaño:
        j = i + 1
        while j < tamaño:
            if nums[i] == nums[j]:
                return True
            j += 1
        i += 1
    return False
           
            
nums = [1,2,3,1]
print(containsDuplicate(nums))



            
            
            
    
            
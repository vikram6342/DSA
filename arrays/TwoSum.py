from typing import List

def bruteTwoSum(nums : List[int], target : int) -> List[int]:

    i =  0
    while i < len(nums):
        j = i + 1
        while j < len(nums):

            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1     
               
        i +=1
        
        
def optimisedTwoSum(nums : List[int], target : int) -> List[int]:
    
    i =  0
    memo = dict()
    while i < len(nums):

        if target - nums[i] in memo:
            return [i, memo[target - nums[i]]]

        memo[nums[i]] = i
        i += 1
        
        
### These soln are valid only because of the following statement

# You may assume that each input would have exactly one solution, and you may not use the same element twice.



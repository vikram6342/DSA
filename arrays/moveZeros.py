from typing import List

"""
Inplace solution
"""

def moveZeroes(self, nums: List[int]) -> None:
    """
    TC -> O(N)
    SC -> O(1)
    """
    fast, slow = 0, 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1
    while slow < len(nums):
        nums[slow] = 0
        slow += 1



def moveZeroes(self, nums: List[int]) -> None:
    """
    TC -> O(N)
    SC -> O(1)
    """
    i, j = 0, 0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    

        
    
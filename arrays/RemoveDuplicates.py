from typing import List

def removeDuplicates(nums : List[int]) -> int:
    """"
    Optimised soln with the time complexity O(n)
    """
    i, j = 1, 0
    while i < len(nums):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j + 1


def removeDuplicates(nums : List[int]) -> int:
    """
    Brute force solution with time complexity O(n) + O(k) -> O(n) as n is always greater than k
    """
    ans = []
    ans.append(nums[0])
    i = 1
    while i < len(nums):
        if nums[i] != nums[i - 1]:
            ans.append(nums[i])
        i += 1
    
    i = 0
    while i < len(ans):
        nums[i] = ans[i]
        i += 1
    return len(ans)
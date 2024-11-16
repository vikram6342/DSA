from typing import List

def pivotIndex(self, nums: List[int]) -> int:
    """
    TC -> O(N * N)
    SC -> O(1)
    """
    leftSum = 0
    for ind, num in enumerate(nums):
        j = ind + 1
        rightSum = 0
        while j < len(nums):
            rightSum += nums[j]
            j += 1
        if leftSum == rightSum:
            return ind
        leftSum += nums[ind]
    return -1

def pivotIndex(self, nums: List[int]) -> int:
    """
    TC -> O(N)
    SC -> O(1)
    """
    leftSum = 0
    total = sum(nums)
    for ind, num in enumerate(nums):
        total -= num
        if total == leftSum:
            return ind
        leftSum += num
    return -1
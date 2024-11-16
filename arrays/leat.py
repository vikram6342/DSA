from typing import List

def largestInd(self, nums: List[int]) -> int:
    """
    TC -> O(N)
    SC -> O(1) As no additional space is used
    """
    larInd = 0
    for i in range(len(nums)):
        if nums[larInd] < nums[i]:
            larInd = i
    for i in range(len(nums)):
        if nums[i] * 2 > nums[larInd] and i != larInd:
            return -1
    return larInd


def dominantIndex(self, nums: List[int]) -> int:
    """
    Dont use this it is just for fun (An unreadable version of Above solution)
    TC -> O(N)
    SC -> O(2) - O(1) as a constant space is used
    """
    ds = [0, 1] if nums[1] > nums[0] else [1, 0]
    i = 2
    while i < len(nums):
        if nums[i] > nums[ds[1]]:
            ds[0], ds[1] = ds[1], i
        elif nums[ds[0]] < nums[i]:
            ds[0] = i
        i += 1
    if nums[ds[0]] * 2 > nums[ds[1]]:
        return -1
    return ds[1]
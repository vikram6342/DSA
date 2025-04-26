from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    i = 0
    ans = []
    while i < len(nums) - 2:
        if i != 0 and nums[i] == nums[i - 1]:
            i += 1
            continue
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])
                while j < k  and nums[j + 1] == nums[j]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1
            else:
                j += 1
        i += 1
    return ans

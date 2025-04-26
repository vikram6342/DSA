from typing import List

def optimalSubarraySum(nums: List[int], k: int) -> int:
    count, pre_sum = 0, 0
    preMap = {0 : 1}
    for num in nums:
        pre_sum += num
        count += preMap.get(pre_sum - k, 0)
        preMap[pre_sum] = preMap.get(pre_sum, 0) + 1
    return count


def bruteSubarraySum(nums: List[int], k: int) -> int:
    count = 0
    for i in range(len(nums)):
        sub_array_sum = 0
        for j in range(i, len(nums)):
            sub_array_sum += nums[j]
            if sub_array_sum == k:
                count += 1
    return count


print(optimalSubarraySum([1,1,1], 2))
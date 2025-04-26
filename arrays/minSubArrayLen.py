from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    ans = float("+inf")
    start = 0
    cur_sum = 0
    for ind, num in enumerate(nums):
        cur_sum += num
        while cur_sum >= target:
            window_size = ind - start + 1
            if window_size < ans:
                ans = window_size
            cur_sum -= nums[start]
            start += 1
    return ans if ans != float("+inf") else 0

print(minSubArrayLen(4, [1,4,4]))
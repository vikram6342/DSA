from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    pre_prod, post_prod = [1 for i in nums], [1 for i in nums]
    for i in range(1, len(nums)):
        pre_prod[i] = pre_prod[i-1] * nums[i - 1]
    for i in range(len(nums)- 2, -1, -1):
        post_prod[i] = post_prod[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        pre_prod[i] *= post_prod[i]
    return pre_prod


print(productExceptSelf([-1,1,0,-3,3]))
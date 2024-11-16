from typing import List


def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    """
    TC -> O(N)
    SC -> O(1)
    """
    ans = []
    maxOnes = 0
    for i in nums:
        if i == 0:
            ans.append(maxOnes)
            maxOnes = 0
        else:
            maxOnes += 1
    ans.append(maxOnes)
    return max(ans)

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    """
    TC -> O(N)
    SC -> O(1)
    """
    total = 0
    maxOnes = 0
    for i in nums:
        if i == 0:
            if total > maxOnes:
                maxOnes = total
            total = 0
        else:
            total += 1
    if total > maxOnes:
        maxOnes = total     
    return maxOnes

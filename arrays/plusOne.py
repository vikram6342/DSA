from typing import List

def plusOne(digits : List[int]) -> List[int]:
    """
    Optimised solution with time complexity O(n)
    """
    
    lastInd = len(digits) - 1
    while lastInd >= 0:
        if digits[lastInd] != 9:
            digits[lastInd] += 1
            return digits
        digits[lastInd] = 0
        lastInd -= 1
    
    return [1] + digits
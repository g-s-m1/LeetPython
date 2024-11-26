from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        result = [(i + extraCandies) >= maxCandies for i in candies]
        return result
        
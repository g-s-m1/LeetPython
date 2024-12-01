from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        answer=[]
        answer.append([i for i in set_nums1 if i not in set_nums2])
        answer.append([i for i in set_nums2 if i not in set_nums1])
        return answer

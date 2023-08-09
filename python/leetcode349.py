"""
两个数组的交集

给定两个数组，编写一个函数来计算它们的交集


"""

class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1)&set(nums2))



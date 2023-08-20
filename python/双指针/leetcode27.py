"""
27. 移除元素
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # 快慢指针:fast,slow初始为0，# slow 用来收集不等于 val 的值，
        # 如果 fast 对应值不等于 val，则把它与 slow 替换
        fast, slow, size = 0, 0, len(nums)
        while fast < size:
            # 不加=,防止越界
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1
        return slow

"""
209. 长度最小的子数组
https://leetcode.cn/problems/minimum-size-subarray-sum/

"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start, end, n, sum = 0, 0, len(nums), 0
        ans = n + 1
        if not nums:  #
            return 0
        while end < n:
            sum += nums[end]
            while sum >= target:  #
                # 　记录当前长度然后出队
                ans = min(ans, end - start + 1)
                sum -= nums[start]
                start += 1

            end += 1
        return 0 if ans == n + 1 else ans

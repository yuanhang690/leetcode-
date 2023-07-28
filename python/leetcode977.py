"""
977. 有序数组的平方
https://leetcode.cn/problems/squares-of-a-sorted-array/
方法二思路：
使用两个指针分别指向位置0 和n-1
每次比较两个指针对应的数,选择较大的那个逆序放入答案并移动指针
"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # ans = []
        # for i in nums:
        #     ans.append(i * i)
        # ans.sort()
        # return ans
        # 解法二：双指针
        n = len(nums)
        ans = [0] * n
        i, j, pos = 0, n - 1, n - 1
        while i <= j:
            if nums[i] * nums[i] < nums[j] * nums[j]:
                ans[pos] = nums[j] * nums[j]
                j -= 1
            else:
                ans[pos] = nums[i] * nums[i]
                i += 1
            pos -= 1
        return ans


solution = Solution()
ans = solution.sortedSquares([-7, -3, 2, 3, 11])
print(ans)

"""
347.前 K 个高频元素

给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

示例 1:

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
"""
import heapq
from operator import length_hint


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # 哈希表
        n = len(nums)
        dic = {}
        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        res = []

        while k > 0:
            tmp = 0
            for num in dic:
                if dic[num] > tmp:
                    tmp = dic[num]
                    cur = num
            dic[cur] = -1
            res.append(cur)
            k -= 1
        return res


solu = Solution()

nums = [1, 1, 1, 2, 2, 3]
res = solu.topKFrequent(nums=nums, k=2)
print(res)

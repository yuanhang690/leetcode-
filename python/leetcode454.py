"""

四数相加 II
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -2^28 到 2^28 - 1 之间，最终结果不会超过 2^31 - 1 。




"""

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # 思路：分nums1，nums2为一组，后两个为一组，将前两个的和存入哈希表，后两个的和的相反数如果也在，
        # 说明这是一个结果
        hash = {}
        for i in nums1:
            for j in nums2:
                # 统计数量
                if i + j in hash:
                    hash[i+j] +=1
                else:
                    hash[i+j] = 1
        
        # 后两组:
        ans = 0
        for v in nums3:
            for u in nums4:
                count = v + u
                if (0-count) in hash:
                    ans += hash[0-count]
        return ans



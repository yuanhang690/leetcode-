class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        l = 0
        for r in range(0, n):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l


solution = Solution()
lst = [0, 1, 2, 2, 3, 0, 4, 2]
print(solution.removeElement(lst, 2))

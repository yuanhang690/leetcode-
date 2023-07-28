class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # nums.sort()
        # n = len(nums)
        # for i in range(0,n):
        #     if nums[i]==nums[i+1]:
        #         return True
        # return False
        #法二
        # nums.sort()
        # n = len(nums)
        # hash = set()
        # for i in range(0,n):
        #     if nums[i] in hash:
        #         return True
        #     hash.add(nums[i])
        # return False
        # 法三
        return not len(set(nums)) ==len(nums)


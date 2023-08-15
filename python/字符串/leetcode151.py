class Solution:
    def reverseWords(self, s: str) -> str:
        # s = s.strip()
        # s_lst = s.split()
        # left, right = 0, len(s_lst) - 1
        # while left <= right:
        #     s_lst[left], s_lst[right] = s_lst[right], s_lst[left]
        #     left += 1
        #     right -= 1
        # return " ".join(s_lst)

        # 双指针法：
        s = s.strip()  # 去除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -= 1
            # 将刚好约过的单词加入res
            res.append(s[i + 1 : j + 1])
            # 越过多余空格
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i
        return " ".join(res)


solution = Solution()
s = "the sky is blue"
res = solution.reverseWords(s)
print(res)

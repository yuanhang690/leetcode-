"""
344. 反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题
eg:
    输入：s = ["h","e","l","l","o"]
    输出：["o","l","l","e","h"]

"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        # n = len(s)
        # mid = n//2
        # for i in range(mid):
        #     # 将第i位的字符与第n-1-i位的字符交换，直到长度为数组一半时正好置换完成
        #     temp = s[i]
        #     s[i] = s[n-1-i]
        #     s[n-1-i] = temp

        # # print(s)
        # 解法二：双指针
        r = len(s) - 1
        l = 0
        while l <= r:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        print(s)


solution = Solution()

s = ["h", "e", "l", "l", "o"]
print("hell world")
solution.reverseString(s)

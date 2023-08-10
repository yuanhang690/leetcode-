"""
202.快乐数
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。

解题重点：
题目说了可能会无限循环，也就是说求和过程中sum可能会重复出现。
考虑使用哈希法，来判断这个sum是否重复出现，如果重复了就是return false， 否则一直找到sum为1为止。

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # 创建哈希表
        hash = set()
        while n not in hash:
            #　每次求完和的结果不在hash里就添加进去
            hash.add(n)
            n_str = str(n)
            # new_num记录求和结果
            new_num = 0
            for i in n_str:
                new_num +=int(i)**2
            if new_num==1:
                return True
            else:
                n = new_num
        return False

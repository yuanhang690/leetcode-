class Solution:
    def generateMatrix(self, n: int) -> [[int]]:
        (
            l,
            r,
            t,
            b,
        ) = (
            0,
            n - 1,
            0,
            n - 1,
        )
        mar = [[0 for _ in range(n)] for _ in range(n)]
        num, tar = 1, n * n
        while num <= tar:
            for i in range(l, r + 1):
                mar[t][i] = num
                num += 1

            t += 1
            for i in range(t, b + 1):
                mar[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):  # right to left
                mar[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):  # bottom to top
                mar[i][l] = num
                num += 1
            l += 1
        return mar

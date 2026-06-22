class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            if (n % 2) == 1:
                res += 1
            else:
                res += 0
            n = n // 2

        return res
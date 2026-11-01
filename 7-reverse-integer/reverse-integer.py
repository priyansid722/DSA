class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        limit = 2**31 if x < 0 else 2**31 - 1   # largest allowed magnitude
        x = abs(x)

        rev = 0
        while x:
            x, pop = divmod(x, 10)

            # rev * 10 + pop must not exceed limit
            if rev > limit // 10 or (rev == limit // 10 and pop > limit % 10):
                return 0

            rev = rev * 10 + pop

        return sign * rev
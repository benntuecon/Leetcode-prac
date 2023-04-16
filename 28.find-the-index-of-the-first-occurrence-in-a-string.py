#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class DoubleHasher:
    def __init__(self, radix1, radix2, mod1, mod2):
        self.radix1, self.radix2 = radix1, radix2
        self.mod1, self.mod2 = mod1, mod2

    def hash(self, s):
        h1, h2 = 0, 0
        for c in s:
            h1, h2 = self.add(h1, h2, c)
        return h1, h2

    def add(self, h1, h2, c):
        h1 = (h1 * self.radix1 + ord(c)-97) % self.mod1
        h2 = (h2 * self.radix2 + ord(c)-97) % self.mod2
        return h1, h2

    def minus(self, h1, h2, c, length):
        h1 = (h1 - (ord(c) - 97) * (self.radix1 ** (length-1))) % self.mod1
        h2 = (h2 - (ord(c) - 97) * (self.radix2 ** (length-1))) % self.mod2
        return h1, h2


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n > m:
            return -1
        radix1, radix2 = 26, 27
        mod1, mod2 = 10**9 + 7, 10**9+33
        dh = DoubleHasher(radix1, radix2, mod1, mod2)
        target, curr = dh.hash(needle), dh.hash(haystack[:n])
        if target == curr:
            return 0
        for i in range(m - n):
            # remove index i, and add index i + n
            curr = dh.minus(*curr, haystack[i], n)
            curr = dh.add(*curr, haystack[i+n])
            if target == curr:
                return i + 1

        return -1
        # @lc code=end

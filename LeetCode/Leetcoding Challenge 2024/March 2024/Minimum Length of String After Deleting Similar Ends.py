
class Solution:
    def minimumLength(self, s: str) -> int:

        n = len(s)
        l,r = 0, n -1

        while l < r and s[l] == s[r]:
            tmp = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1

        return (r - l + 1)


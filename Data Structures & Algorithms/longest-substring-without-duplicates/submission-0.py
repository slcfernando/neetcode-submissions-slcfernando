class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l, r = 0, 0

        # increasing size of window
        uniqueLetters = set()
        while r < len(s):
            while s[r] in uniqueLetters:
                uniqueLetters.remove(s[l])
                l += 1
            uniqueLetters.add(s[r])
            r += 1
            maxLength = max(maxLength, r - l)
        return maxLength
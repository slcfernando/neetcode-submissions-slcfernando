class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for n in numSet:
            length = 0
            if n - 1 not in numSet:
                length = 1
                i = n
                while (i := i + 1) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
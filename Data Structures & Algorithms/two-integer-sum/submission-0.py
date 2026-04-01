class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash:
                return sorted([i, hash[complement]])
            hash[n] = i
        raise ValueError
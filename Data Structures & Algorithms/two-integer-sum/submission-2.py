class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # store in a dictionary the numbers as keys and their indices as values
        numIndices = {}

        # check numIndices if a number's complement exists
        for i, n in enumerate(nums):
            complement = target - n
            # if so, return the pair's indices
            # this works even if the complement is the same as n, because n hasn't been stored yet
            if complement in numIndices:
                return [numIndices[complement], i]
            
            # else, keep track of the number's index in numIndices
            numIndices[n] = i

        return ValueError